import frappe
from datetime import datetime

@frappe.whitelist()
def update_asset_schedule_dates(method=None):
    assets = frappe.get_all("Asset", fields=["name"])

    for asset in assets:
        asset_doc = frappe.get_doc("Asset", asset["name"])
        updated = False

        # Step 1: Get all Asset Depreciation Schedule records for the asset
        ads_records = frappe.get_all("Asset Depreciation Schedule",
            filters={"asset": asset_doc.name},
            fields=["name"]
        )

        for ads in ads_records:
            # Step 2: Get child table entries from Depreciation Schedule
            schedules = frappe.get_all("Depreciation Schedule",
                filters={"parent": ads["name"]},
                fields=["name", "schedule_date"]
            )

            for schedule in schedules:
                schedule_date = schedule.schedule_date

                if isinstance(schedule_date, str):
                    schedule_date = datetime.strptime(schedule_date, "%Y-%m-%d").date()

                if schedule_date.day != 25:
                    new_schedule_date = schedule_date.replace(day=25)

                    frappe.db.sql("""
                        UPDATE `tabDepreciation Schedule`
                        SET schedule_date = %s
                        WHERE name = %s AND journal_entry IS NULL
                    """, (new_schedule_date, schedule["name"]))

                    updated = True

        if updated:
            frappe.db.commit()


@frappe.whitelist()
def update_asset_schedule_date(doc, event):
    if doc.doctype != "Asset":
        return

    updated = False

    # Same steps as above
    ads_records = frappe.get_all("Asset Depreciation Schedule",
        filters={"asset": doc.name},
        fields=["name"]
    )

    for ads in ads_records:
        schedules = frappe.get_all("Depreciation Schedule",
            filters={"parent": ads["name"]},
            fields=["name", "schedule_date"]
        )

        for schedule in schedules:
            schedule_date = schedule.schedule_date

            if isinstance(schedule_date, str):
                schedule_date = datetime.strptime(schedule_date, "%Y-%m-%d").date()

            if schedule_date.day != 25:
                new_schedule_date = schedule_date.replace(day=25)
                new_schedule_date_str = new_schedule_date.strftime("%Y-%m-%d")

                frappe.db.sql("""
                    UPDATE `tabDepreciation Schedule`
                    SET schedule_date = %s
                    WHERE name = %s AND journal_entry IS NULL
                """, (new_schedule_date_str, schedule["name"]))

                updated = True

    if updated:
        frappe.db.commit()
