from . import __version__ as app_version

app_name = "navari_kayes"
app_title = "Navari Kayes"
app_publisher = "Navari Limited"
app_description = "Reports and customizations for Kayes"
app_email = "info@navari.co.ke"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/navari_kayes/css/navari_kayes.css"
# app_include_js = "/assets/navari_kayes/js/navari_kayes.js"

# include js, css files in header of web template
# web_include_css = "/assets/navari_kayes/css/navari_kayes.css"
# web_include_js = "/assets/navari_kayes/js/navari_kayes.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "navari_kayes/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "navari_kayes.utils.jinja_methods",
#	"filters": "navari_kayes.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "navari_kayes.install.before_install"
# after_install = "navari_kayes.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "navari_kayes.uninstall.before_uninstall"
# after_uninstall = "navari_kayes.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "navari_kayes.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Journal Entry": {
		"on_cancel": "navari_kayes.controllers.cancel_linked_cost_distributions.custom_on_cancel"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"navari_kayes.tasks.all"
#	],
#	"daily": [
#		"navari_kayes.tasks.daily"
#	],
#	"hourly": [
#		"navari_kayes.tasks.hourly"
#	],
#	"weekly": [
#		"navari_kayes.tasks.weekly"
#	],
#	"monthly": [
#		"navari_kayes.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "navari_kayes.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "navari_kayes.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "navari_kayes.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]
auto_cancel_exempted_doctypes = ["Cost Distribution"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]
ignore_links_on_delete = ["Cost Distribution"]

# Request Events
# ----------------
# before_request = ["navari_kayes.utils.before_request"]
# after_request = ["navari_kayes.utils.after_request"]

# Job Events
# ----------
# before_job = ["navari_kayes.utils.before_job"]
# after_job = ["navari_kayes.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"navari_kayes.auth.validate"
# ]
