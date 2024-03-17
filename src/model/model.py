import tensorflow as tf

class MyModel:
    def __init__(self, input_shape, seq_length = 25, learning_rate=0.005):
        """ initializer """

        ## set basic self
        self.input_shape = input_shape
        self.seq_length = seq_length
        self.learning_rate = learning_rate

    def build_model(self, ne_size = 128):
        """ model """

        ## input
        inputs = tf.keras.Input(self.input_shape)
        x = tf.keras.layers.LSTM(ne_size)(inputs)

        ## output
        outputs = {
            'pitch': tf.keras.layers.Dense(ne_size, name='pitch')(x),
            'step': tf.keras.layers.Dense(1, name='step')(x),
            'duration': tf.keras.layers.Dense(1, name='duration')(x),
        }

        ## build
        model = tf.keras.Model(inputs, outputs)
        return model

    def compile_model(self, model):
        """ compiler """
        
        loss = {
            'pitch': tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            'step': mse_with_positive_pressure,
            'duration': mse_with_positive_pressure,
        }

        optimizer = tf.keras.optimizers.Adam(learning_rate=self.learning_rate)

        model.compile(loss=loss, 
                    optimizer=optimizer,
                    loss_weights={
                    'pitch': 0.05,
                    'step': 1.0,
                    'duration':1.0,
                    })
        return model

    def get_summary(self, model):
        return model.summary()


# Custom loss function for positive pressure
def mse_with_positive_pressure(y_true, y_pred):
    return tf.reduce_mean(tf.square(tf.maximum(0.0, y_pred - y_true)))


# Example usage:
if __name__ == "__main__":
    seq_length = 25
    input_shape = (seq_length, 3)
    learning_rate = 0.005
    seq_length = 100

    model_builder = MyModel(input_shape, seq_length, learning_rate)
    model = model_builder.build_model()
    compiled_model = model_builder.compile_model(model)
    summary = model_builder.get_summary(compiled_model)
