import frappe

def capture_original_name(doc, method):
    # リクエストのアップロード元名を保持（存在すれば）
    orig = frappe.form_dict.get("file_name") or doc.file_name
    doc.original_file_name = orig