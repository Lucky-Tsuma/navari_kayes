# Copyright (c) 2023, Navari Limited and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from pypika import Criterion

def execute(filters=None):
	if filters.from_date > filters.to_date:
		frappe.throw(_("From Date cannot be greater than To Date"));
	return get_columns(), get_data(filters);

def get_columns():
	return [
		{
			'fieldname': 'purchase_order',
			'label': _('PO #'),
			'fieldtype': 'Link',
			'options': 'Purchase Order',
			'width': 200
		},
		{
			'fieldname': 'cost_center',
			'label': _('Dept'),
			'fieldtype': 'Link',
			'options': 'Cost Center',
			'width': 200
		},
		{
			'fieldname': 'description',
			'label': _('Description'),
			'fieldtype': 'Data',
			'width': 240
		},
		{
			'fieldname': 'supplier',
			'label': _('Supplier'),
			'fieldtype': 'Link',
			'options': 'Supplier',
			'width': 200
		},
		{
			'fieldname': 'expected_shipping_date',
			'label': _('Expected Shipping Date'),
			'fieldtype': 'Date',
			'width': 200
		},
		{
			'fieldname': 'expected_arrival_date',
			'label': _('Expected Arrival Date'),
			'fieldtype': 'Date',
			'width': 200
		},
		{
			'fieldname': 'shipping_terms_and_method',
			'label': _('Shipping Terms/Method'),
			'fieldtype': 'Link',
			'options': 'Incoterm',
			'width': 200
		},
		{
			'fieldname': 'customer_name',
			'label': _('Customer Name'),
			'fieldtype': 'Link',
			'options': 'Customer',
			'width': 240
		},
		{
			'fieldname': 'delivery_place',
			'label': _('Delivery Place'),
			'fieldtype': 'Link',
			'options': 'Address',
			'width': 150
		},
		{
			'fieldname': 'shipping_info',
			'label': _('Shipping Info'),
			'fieldtype': 'Data',
			'width': 150
		},
		{
			'fieldname': 'customer_delivery_deadline',
			'label': _('Customer Delivery Deadline'),
			'fieldtype': 'Date',
			'width': 200
		},
		{
			'fieldname': 'comments',
			'label': _('Comments'),
			'fieldtype': 'Data',
			'width': 150
		}
	];

def get_data(filters):
	from_date = filters.get('from_date');
	to_date = filters.get('to_date');

	purchase_order = frappe.qb.DocType("Purchase Order");
	purchase_order_item = frappe.qb.DocType("Purchase Order Item");
	sales_order = frappe.qb.DocType("Sales Order");

	conditions = [purchase_order.transaction_date[from_date:to_date]];

	if filters.get('company'):
		conditions.append(purchase_order.company == filters.get('company'));
	if filters.get('purchase_order'):
		conditions.append(purchase_order.name == filters.get('purchase_order'));
	if filters.get('supplier'):
		conditions.append(purchase_order.supplier == filters.get('supplier'));
	if filters.get('cost_center'):
		conditions.append(purchase_order_item.cost_center == filters.get('cost_center'));
	if filters.get('customer'):
		conditions.append(purchase_order.customer == filters.get('customer'));

	query = frappe.qb.from_(purchase_order)\
		.inner_join(purchase_order_item)\
		.on(purchase_order.name == purchase_order_item.parent)\
		.left_join(sales_order)\
		.on(purchase_order_item.sales_order == sales_order.name)\
		.select(
			purchase_order.name.as_("purchase_order"),
			purchase_order.supplier.as_("supplier"),
			purchase_order.incoterm.as_("shipping_terms_and_method"),
			purchase_order_item.cost_center.as_("cost_center"),
			purchase_order_item.description.as_("description"),
			purchase_order_item.schedule_date.as_("expected_shipping_date"),
			purchase_order_item.expected_delivery_date.as_("expected_arrival_date"),
			purchase_order_item.sales_order.as_("sales_order"),
			purchase_order_item.sales_order_item.as_("sales_order_item"),
			sales_order.customer_address.as_("delivery_place"),
			sales_order.shipping_info.as_("shipping_info")
		).where(Criterion.all(conditions))
	
	shipment_details = query.run(as_dict=True);

	if shipment_details:
		for row in shipment_details:
			if row.get('sales_order'):
				row['customer_delivery_deadline'] = frappe.db.get_value('Sales Order', row.get('sales_order'), 'delivery_date');
				row['comments'] = frappe.db.get_value('Sales Order', row.get('sales_order'), 'comments');
				row['customer_name'] = frappe.db.get_value('Sales Order', row.get('sales_order'), 'customer');
				if not row.get('shipping_terms_and_method'):
					row['shipping_terms_and_method'] = frappe.db.get_value('Sales Order', row.get('sales_order'), 'incoterm');
		return shipment_details;
	else:
		return [];