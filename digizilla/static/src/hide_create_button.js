/** @odoo-module **/

import { FormController } from "@web/views/form/form_controller";
import { patch } from "@web/core/utils/patch";

patch(FormController.prototype, {
    setup() {
        super.setup(...arguments);
        if (this.props.resModel === "digizilla.record") {
            // This is the specific way to disable actions in v17
            this.activeActions.create = false;
        }
    },
});