/** @odoo-module */

import {registry} from "@web/core/registry";
import {BooleanField} from "@web/views/fields/boolean/boolean_field";

class LateOrderBooleanField extends BooleanField {
    // 构造函数
    constructor() {
        super(...arguments);
        this.stateText = this.props.value ? "已选中" : "未选择"; // 初始化状态文本
    }

    onChange(event) {
        const newValue = event.target.checked; // 获取新的复选框状态
        this.props.update(newValue); // 更新状态
        this.stateText = newValue ? "已选中" : "未选择"; // 更新状态文本
    }

    stopPropagation(event) {
        event.stopPropagation(); // 阻止事件冒泡，避免触发跳转
    }


    // 渲染方法
    getTemplate() {
        console.log("getTemplate called"); // 添加调试日志
        return `
            <div class="custom-boolean-field">
                <input
                    type="checkbox"
                    t-att-checked="props.value"
                    t-on-change="onChange"
                    t-on-click="preventDoubleClick"
                    class="custom-checkbox"
                />
                <span class="status-text" t-esc="stateText"></span>
            </div>
        `;
    }

    // 防止双击事件
    preventDoubleClick(event) {
        if (this.isDoubleClick) {
            event.preventDefault();
        }
        this.isDoubleClick = !this.isDoubleClick; // Toggle state
        setTimeout(() => this.isDoubleClick = false, 300); // 300ms内无法再次点击
    }
}

// 为组件设置模板
LateOrderBooleanField.template = "custom_boolean_style.LateOrderBooleanField";

registry.category("fields").add("late_boolean", LateOrderBooleanField);
