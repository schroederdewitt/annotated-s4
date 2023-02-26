import jax
import matplotlib.pyplot as plt
from s4 import BatchStackedModel, S4Layer, sample_checkpoint


# sample_image_prefix,
# from .s4d import S4DLayer


#rng = jax.random.PRNGKey(1)
rng = jax.random.PRNGKey(2)




def DefaultMNIST(l):
    layer_args = {}
    layer_args["N"] = 64
    layer_args["l_max"] = 784

    # TODO -> Read this from file information.?
    # model = S4DLayer
    # model = BatchStackedModel(
    #     layer_cls=model,
    #     layer=layer_args,
    #     d_output=256,
    #     d_model=512,
    #     n_layers=6,
    #     prenorm=True,
    #     classification=False,
    #     decode=True,
    #     training=False
    # )
    # model = S4Layer
    # model = BatchStackedModel(
    #     layer_cls=model,
    #     layer=layer_args,
    #     d_output=256,
    #     d_model=512,
    #     n_layers=6,
    #     prenorm=False,
    #     classification=False,
    #     decode=True,
    #     training=False,
    # )

    # SMALL
    # model = S4Layer
    # model = BatchStackedModel(
    #    layer_cls=model,
    #    layer=layer_args,
    #    d_output=256,
    #    d_model=128,
    #    n_layers=6,
    #    prenorm=True,
    #    classification=False,
    #    decode=True,
    #    training=False,
    # )

    # LARGE
    model = S4Layer
    model = BatchStackedModel(
       layer_cls=model,
       layer=layer_args,
       d_output=256,
       d_model=512,
       n_layers=6,
       prenorm=True,
       classification=False,
       decode=True,
       training=False,
       embedding=True
    )
    return model


MNIST_LEN = 784
# default_train_path = "best_16"
# default_train_path = "checkpoints/mnist/{'d_model': 512, 'n_layers': 6, 'dropout': 0.0, 'prenorm': True, 'layer': {'N': 64, 'l_max': 784}}-d_model=512-lr=0.004-bsz=32/"
# default_train_path = "checkpoints/mnist/s4-d_model=128-lr=0.001-bsz=128/"
# default_train_path = "/home/srush/best_13"

# default_train_path = "checkpoints/mnist/s4-d_model=512-lr=0.005-bsz=50/"
# default_train_path = "checkpoints/cifar/s4-d_model=128-lr=0.005-bsz=128/"
default_train_path = "checkpoints/cifar/s4-d_model=512-lr=0.005-bsz=50/"

out = sample_checkpoint(
    default_train_path, DefaultMNIST(MNIST_LEN), MNIST_LEN, rng
)
plt.imshow(out.reshape(28, 28))
plt.savefig("sample.png")

# out = sample_mnist_prefix(default_train_path, DefaultMNIST(MNIST_LEN), MNIST_LEN, rng)
