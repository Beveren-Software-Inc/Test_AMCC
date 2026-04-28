frappe.ui.form.on("Purchase Order", {
  before_workflow_action: (frm) => {
      console.log(frm.selected_workflow_action);
      if (frm.doc.workflow_state === "Pending For Manager") {
          frm.set_value("po_manager_name", frappe.session.user);
          frm.set_value("pom_date", frappe.datetime.nowdate());

      }
      else if(frm.doc.workflow_state === "Pending For FC Approval"){
          
              frm.set_value("fc_name", frappe.session.user);
              frm.set_value("fcm_date", frappe.datetime.nowdate());


      }
      else if(frm.doc.workflow_state === "Pending For GM Approval"){
              frm.set_value("gm_approver_name", frappe.session.user);
              frm.set_value("gmm_date", frappe.datetime.nowdate());
  

      }
      
  },

});




