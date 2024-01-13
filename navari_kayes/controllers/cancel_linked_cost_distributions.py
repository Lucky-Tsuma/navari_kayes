import frappe

def custom_on_cancel(doc, method=None):
    cost_distributions = []
    for x in doc.get('accounts'):
        if x.cost_distribution and x.cost_distribution not in cost_distributions:
            cost_distributions.append(x.cost_distribution)

    for cost_distribution in cost_distributions:
        try:
            frappe.db.sql(f"""
                UPDATE `tabCost Distribution`
                SET docstatus = 2
                WHERE name = '{cost_distribution}'
            """)
        except Exception as e:
            frappe.msgprint(f"Error cancelling cost distribution {cost_distribution}: {str(e)}")
            frappe.log_error(f"Error cancelling cost distribution {cost_distribution}: {str(e)}")