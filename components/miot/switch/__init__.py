from esphome.components import switch
import esphome.config_validation as cv
import esphome.codegen as cg
from .. import miot_ns, CONF_MIOT_ID, CONF_MIOT_SIID, CONF_MIOT_PIID, CONF_MIOT_POLL, Miot

DEPENDENCIES = ["miot"]

MiotSwitch = miot_ns.class_("MiotSwitch", switch.Switch, cg.Component)

CONFIG_SCHEMA = (
    switch.switch_schema(MiotSwitch)
    .extend(
        {
            cv.GenerateID(CONF_MIOT_ID): cv.use_id(Miot),
            cv.Required(CONF_MIOT_SIID): cv.uint32_t,
            cv.Required(CONF_MIOT_PIID): cv.uint32_t,
            cv.Optional(CONF_MIOT_POLL, default=True): cv.boolean,
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
)

async def to_code(config):
    var = await switch.new_switch(config)
    await cg.register_component(var, config)

    parent = await cg.get_variable(config[CONF_MIOT_ID])
    cg.add(var.set_miot_config(parent, config[CONF_MIOT_SIID], config[CONF_MIOT_PIID], config[CONF_MIOT_POLL]))