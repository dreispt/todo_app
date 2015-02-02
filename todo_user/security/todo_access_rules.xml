<?xml version="1.0" encoding="utf-8"?>
<openerp>
  <data noupdate="0">

    <delete model="ir.rule"
            search="[('id', 'in', ref('todo_app.todo_task_user_rule'))]" />

    <record id="todo_task_per_user_rule" model="ir.rule">
        <field name="name">ToDo Tasks only for owner</field>
        <field name="model_id" ref="model_todo_task"/>
        <field name="groups" eval="[(4, ref('base.group_user'))]"/>
        <field name="domain_force">
          ['|',('user_id','in',[user.id,False]),
               ('message_follower_ids','in',[user.partner_id.id])
          ]
        </field>
    </record>

  </data>
</openerp>
