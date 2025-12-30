odoo.define('digizilla.hide_create', function (require) {
    "use strict";

    const FormController = require('web.FormController');

    FormController.include({
        _updateButtons: function () {
            this._super.apply(this, arguments);
            if (this.$buttons) {
                this.$buttons.find('.o_form_button_create').hide();
            }
        },
    });
});