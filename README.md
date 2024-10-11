# custom_boolean_style 模块

## 效果图
![image](https://github.com/user-attachments/assets/bfefe1fa-b015-41b1-8053-4dffed539db7)


## 概述

`custom_boolean_style` 模块是 Odoo 的自定义布尔字段实现，提供了一个新的布尔字段组件 `late_boolean`，它具有自定义样式和行为。用户可以通过该模块轻松地在 Odoo 的表单视图中使用该布尔字段。

## 特性

- 自定义布尔字段显示状态文本（"已选中" / "未选择"）。
- 支持点击复选框时阻止事件冒泡，避免触发其他操作。
- 动态更新状态文本，提供实时反馈。
- 选中的时候数据背景呈绿色，未选中的时候数据背景呈白色。

## 安装

1. 将 `custom_boolean_style` 模块克隆或下载到 Odoo 的 `addons` 目录下。
2. 在 Odoo 的应用界面中，更新应用列表。
3. 搜索 `custom_boolean_style`，点击安装。

## 使用方法

要在其他模块中使用 `late_boolean` 布尔字段，请按照以下步骤操作：


### 1. 定义字段

在你的模型中，使用 `late_boolean` 类型定义布尔字段。例如：

```python
from odoo import models, fields

class YourModel(models.Model):
    _name = 'your.model'
    
    # 定义字段
    is_active = fields.Boolean(string='是否活跃')
```

### 2. 更新视图

在相应的 XML 视图文件中，确保你在表单视图中添加了该布尔字段。例如：

```xml
<record id="view_your_model_form" model="ir.ui.view">
    <field name="name">your.model.form</field>
    <field name="model">your.model</field>
    <field name="arch" type="xml">
        <form>
            <sheet>
                <group>
                    <field name="is_active" widget="late_boolean"/> <!-- 使用自定义布尔字段 -->
                </group>
            </sheet>
        </form>
    </field>
</record>
```

### 3. 访问模块

安装和配置完成后，你可以在 Odoo 的表单视图中看到 `late_boolean_field`，并可以通过点击复选框来切换状态。

## 注意事项

- 确保在 Odoo 16 及以上版本中使用该模块。
- 若需要修改样式或功能，请查看 JavaScript 和 CSS 文件以进行自定义。

## 贡献

欢迎任何对 `custom_boolean_style` 模块的贡献和建议！请通过 [GitHub](https://github.com/hongzhe12/custom_boolean_style) 提交问题或拉取请求。

## 许可证

该模块遵循 MIT 许可证。有关更多信息，请参见 LICENSE 文件。


### 说明
1. **模块概述**: 简要介绍模块的功能和特点。
2. **安装说明**: 清楚列出安装步骤。
3. **使用方法**: 详细描述如何在其他模块中引用和使用 `late_boolean` 字段。
4. **注意事项**: 提示用户注意的事项，确保模块在正确的 Odoo 版本上运行。
5. **贡献与许可证**: 提供对贡献的欢迎和许可证信息。

根据具体需求，可以对内容进行调整和扩展。
