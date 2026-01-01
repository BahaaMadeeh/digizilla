/** @odoo-module **/

import { patch } from 'web.utils';
import ListController from 'web.ListController';

patch(ListController.prototype, 'digizilla.hide_create_button', {
    _updateButtons: function () {
        this._super.apply(this, arguments);
        if (this.modelName === 'digizilla.record') {
            this.$buttons.find('.o_list_button_add').hide();
        }
    },
});
