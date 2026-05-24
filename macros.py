import json

def define_env(env):

    @env.macro
    def ContraptionCard(name, img, price, automated):
        return f"- ![{name} image](/assets/{img}) __{name}__<br>Price: ${price}<br>Can be automated: {automated}"