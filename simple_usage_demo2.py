import tfnn
import numpy as np

# make some data
xs = np.linspace(-5, 5, 300)[:, np.newaxis]
ys = xs**2

# define it as tfnn.Data
data = tfnn.Data(xs, ys)

# train test split function
t_data, v_data = data.train_test_split(0.7)

# define network properties
network = tfnn.RegNetwork(n_inputs=data.xs.shape[1], n_outputs=data.ys.shape[1])

# add hidden layer
network.add_hidden_layer(n_neurons=20, activator=tfnn.nn.relu)

# add output layer
network.add_output_layer(activator=None)

# set optimizer. Default GradientDescent
network.set_optimizer(optimizer=tfnn.train.AdamOptimizer(1e-3))

# set evaluator for compute the accuracy, loss etc.
evaluator = tfnn.Evaluator(network)

for i in range(2000):
    b_xs, b_ys = t_data.next_batch(50, loop=True)
    network.run_step(b_xs, b_ys)
    if i % 50 == 0:
        print(evaluator.compute_cost(v_data.xs, v_data.ys))