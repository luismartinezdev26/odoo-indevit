import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class IndevitDashboard extends Component {
    static template = "indevit.Dashboard";
    static props = ["*"];
}

registry.category("actions").add("indevit.dashboard", IndevitDashboard);
