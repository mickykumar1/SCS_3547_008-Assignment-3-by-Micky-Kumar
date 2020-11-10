from pomegranate import *

# Rain node has no parents
rain = Node(DiscreteDistribution({
    "Yes": 0.2,
    "No": 0.8,
}), name="rain")

# Track maintenance node is conditional on rain
maintenance = Node(ConditionalProbabilityTable([
    ["Yes", "yes", 0.4],
    ["No", "no", 0.6],
], [rain.distribution]), name="maintenance")

# Train node is conditional on rain and maintenance
train = Node(ConditionalProbabilityTable([
    ["none", "yes", "on time", 0.8],
    ["none", "yes", "delayed", 0.2],
    ["none", "no", "on time", 0.9],
    ["none", "no", "delayed", 0.1],
    ["light", "yes", "on time", 0.6],
    ["light", "yes", "delayed", 0.4],
    ["light", "no", "on time", 0.7],
    ["light", "no", "delayed", 0.3],
    ["heavy", "yes", "on time", 0.4],
    ["heavy", "yes", "delayed", 0.6],
    ["heavy", "no", "on time", 0.5],
    ["heavy", "no", "delayed", 0.5],
], [rain.distribution, maintenance.distribution]), name="train")



# Create a Bayesian Network and add states
model = BayesianNetwork()
model.add_states(rain, maintenance, train, )

# Add edges connecting nodes
model.add_edge(rain, maintenance)
model.add_edge(rain, train)

# Finalize model
model.bake()
