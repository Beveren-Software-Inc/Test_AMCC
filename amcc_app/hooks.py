from . import __version__ as app_version

app_name = "amcc_app"
app_title = "AMCC App"
app_publisher = "Shivansh"
app_description = "AMCC Custom Development"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "shivansh@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/amcc_app/css/amcc_app.css"
# app_include_js = "/assets/amcc_app/js/amcc_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/amcc_app/css/amcc_app.css"
# web_include_js = "/assets/amcc_app/js/amcc_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "amcc_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views

doctype_js = {
    "Purchase Order" : [
        "public/js/purchase_order.js",
        ],

}


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

# Installation
# ------------

# before_install = "amcc_app.install.before_install"
# after_install = "amcc_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "amcc_app.uninstall.before_uninstall"
# after_uninstall = "amcc_app.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "amcc_app.notifications.get_notification_config"

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
	"Asset": {
		"on_update": "amcc_app.amcc_app.overrides.update_asset_schedule_date.update_asset_schedule_date",
        "on_submit": "amcc_app.amcc_app.overrides.update_asset_schedule_date.update_asset_schedule_date"

}
}
   
# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"

#	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
#		"amcc_app.tasks.all"
#	],
    "daily": [
        "amcc_app.amcc_app.overrides.update_asset_schedule_date.update_asset_schedule_dates"
    ],
#	"daily": [
#		"amcc_app.tasks.daily"
#	],
#	"hourly": [
#		"amcc_app.tasks.hourly"
#	],
#	"weekly": [
#		"amcc_app.tasks.weekly"
#	]
#	"monthly": [
#		"amcc_app.tasks.monthly"
#	]
}




# Testing
# -------

# before_tests = "amcc_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "amcc_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "amcc_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Request Events
# ----------------
# before_request = ["amcc_app.utils.before_request"]
# after_request = ["amcc_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["amcc_app.utils.before_job"]
# after_job = ["amcc_app.utils.after_job"]

# User Data Protection
# --------------------

user_data_fields = [
    {
        "doctype": "{doctype_1}",
        "filter_by": "{filter_by}",
        "redact_fields": ["{field_1}", "{field_2}"],
        "partial": 1,
    },
    {
        "doctype": "{doctype_2}",
        "filter_by": "{filter_by}",
        "partial": 1,
    },
    {
        "doctype": "{doctype_3}",
        "strict": False,
    },
    {
        "doctype": "{doctype_4}"
    }
]
# see if its working


# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"amcc_app.auth.validate"
# ]

fixtures = [
    {"dt": "Property Setter", 
        "filters": [
            [
                "name", "in", {
                    "Purchase Order-items-permlevel",
    

                }
            ]
        ]
    },
    
{"dt": "Custom Field", 
        "filters": [
            [
                "name", "in", {
                    "Purchase Order-approval_section",
                    "Purchase Order-po_manager_name",
                    "Purchase Order-pom_date",
                    "Purchase Order-column_break_duvjp",
                    "Purchase Order-fc_name",
                    "Purchase Order-fcm_date",
                    "Purchase Order-gm_approver_name",
                    "Purchase Order-gmm_date",
                    "Purchase Order-exemption_form"
                                        
                }
            ]
        ]
    }
]