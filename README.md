# Status
- [ ] Minimum viable test suite
- [ ] Alpha release

# The Last Word On App Configuration  

The purpose of this project is to fufill my all the uses I desire from an application
configuration library.

# Usage
## Create a `defaults.yaml` For Your Application

`defaults.yaml` :
```
AGENT:
	LAMBDA: 0.1
	GAMMA: 1
	ALPHA: 0.01
	EPSILON: 0.05

ENV:
	STATE_SPACE:
		- 8
		- 8
	ACTION_SPACE:
		- 3
```

Save it in your project root directory.
```
|-- app
|-- tests
|-- Dockerfile
|-- pyproject.toml
|-- defaults.yaml         <----
|-- main.py
```

## Use Your Config
Use your config as if you wrote the Config object yourself.

```
from .agent import Agent
from fig import Config as C


lambda = C.AGENT_LAMBDA
epsilon = C.AGENT_EPSILON
state_space = C.ENV_STATE_SPACE

agent = Agent(lambda, epsilon, state_space)
...
```

## Override the `defaults` When Desired
Somtimes its necessary to overide the `defaults.yaml`. No need to change the defaults,
pyfig's got you covered.

### Override By File
If you have another config file, you can load it via the cli:
```
python main.py --figfile="better_config.yaml"
```

### Override By Environment Variables
```
export AGENT_LAMBDA=0.9
export AGENT_EPSILON=0.1
python main.py
```

### Override By CLI
```
python main.py --AGENT_LAMBDA=0.9 --AGENT_EPSILON=0.1
```

### Override By All Three
Although not advised, you can if you want to.

The variable loading precedence is as follows:
* defaults get loaded first
* these get overriden by any override files
* these, in turn get overridden by environment variables
* and command line arguments get the last word

# Wishlist

## IO
- [x] Reads YAML files
- [ ] Reads TOML files
- [ ] Reads Environment variables
- [ ] Reads CLI input
- [ ] Variable setting priority according to: ENV + cli first, config file second, defaults third

## Behaviour

- [x] Default values present unless overridden by any of the methods listed above
- [ ] Some sort of way to log the configuration that was loaded. This is necessary
  since there could be so much data flying around
- [x] Accessible from all modules and submodules without explict data passing (like absl-py)
- [x] No global variables, they break everything (not like absl-py)


