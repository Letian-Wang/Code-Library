import tensorflow as tf
import numpy as py
import time
## Basic
    x = tf.zeros([10,10])
    x += 5
    a = tf.matmul([[1]],[[2,3]])
    sess = tf.Session()
    print(a.shape)
    print(sess.run(a))

# constant
    node1 = tf.constant(3.0,tf.float32)
    node2 = tf.constant(4.0)
    node3 = tf.add(node1,node2)
    print(node1)
    print("node1： ", node1, "node2: ",node2)
    print("node3： ", node3)
    sess = tf.Session()
    print("sess.run(node1,node2): ", sess.run([node1,node2]))
    print("sess.run(node3): ", sess.run(node3))

# Placeholder
    a = tf.placeholder(tf.float32)
    b = tf.placeholder(tf.float32)
    adder_node = a + b
    print(sess.run(adder_node, feed_dict={a:3,b:4.5}))
    print(sess.run(adder_node, feed_dict={a:[1,3],b:[2,4]}))

# Check GPU
    x = tf.random.uniform([3,3])
    print('Is there a GPU available')
    print(tf.config.experimental.list_physical_devices("GPU"))
    print('Is the Tensor on GPU #0: ')
    print(x.device.endswith('GPU:0'))

    # Specify CPU or GPU
    def time_matmul(x):
        start = time.time()
        for loop in range(10):
            tf.matmul(x,x)
        result = time.time() - start
        print("10 loops: {:0.2f}ms".format(1000*result))

    # Force on CPU
    print("On CPU:")
    with tf.device("CPU:0"):
        x = tf.random.uniform([1000,1000])
        assert x.device.endswith("CPU:0")
        time_matmul(x)

    # Force on GPU 0 if available
    if tf.config.experimental.list_physical_devices("GPU"):
        print("On GPU:")
        with tf.device("GPU:0"):
            x = tf.random.uniform([1000,1000])
            assert x.device.endswith("GPU:0")
            time_matmul(x)


    print(tf.test.is_gpu_available())

# Gradient
    x = tf.ones((2,2))
    with tf.GradientTape(persistent=True) as t:
        t.watch(x)
        y = tf.reduce_sum(x)
        z = tf.multiply(y,y)

    dz_dx = t.gradient(z,x)
    dz_dy = t.gradient(z,y)
    del t
    sess = tf.Session()
    print(sess.run(dz_dx))
    print(sess.run(dz_dy))

# Gradient after operations
    def f(x,y):
        output = 1.0
        for i in range(y):
            if i > 1 and i < 5:
                output = tf.multiply(output,x)
        return output

    def grad(x,y):
        with tf.GradientTape() as t:
            t.watch(x)
            out = f(x,y)
        return t.gradient(out,x)

    x = tf.convert_to_tensor(2.0)
    sess = tf.Session()
    assert sess.run(grad(x,6)) == 12

# High-order differetion
    x = tf.ones((2,2))
    with tf.GradientTape() as t:
        with tf.GradientTape() as t2:
            y = tf.multiply(x,x)
        dy_dx = t2.gradient(y, x)
    d2y_dx2 = t.gradient(dy_dx, x)
    sess = tf.Session()
    sess.run(dy_dx)

# Linear regression
    x_train = [1,2,3]
    y_train = [1,2,3]
    W = tf.Variable(tf.random_normal([1]), name='weight')
    b = tf.Variable(tf.random_normal([1]), name='bias')

    hypothesis = x_train * W + b

    cost = tf.reduce_mean(tf.square(hypothesis - y_train))
    # minimize
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
    train = optimizer.minimize(cost)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for step in range(2001):
        sess.run(train)
        if step % 20 == 0:
            print(step, sess.run(cost), sess.run(W), sess.run(b))

# Linear regression full code
    W = tf.Variable(tf.random_normal([1]),name='weigth')
    b = tf.Variable(tf.random_normal([1]),name='bias')

    X = tf.placeholder(tf.float32, shape=[None])
    Y = tf.placeholder(tf.float32, shape=[None])

    hypothesis = X * W + b
    cost = tf.reduce_mean(tf.square(hypothesis - Y))
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
    train = optimizer.minimize(cost)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for step in range(2001):
        cost_val, W_val, b_valu, _ = (sess.run([cost, W, b, train], 
        feed_dict = {X:[1,2,3], Y:[1,2,3]}))
        if step % 20 == 0:
            print(step, cost_val, W_val, b_valu)

# Specify CPU or GPU, save and load model
    os.environ["CUDA_VISIBLE_DEVICES"]='0'
    with tf.device('/cpu:0'):
        x_data = np.array([[0,0],[0,1],[1,0],[1,1]], dtype=np.float32)
        y_data = np.array([[0],[1],[1],[0]], dtype=np.float32)
        X = tf.placeholder((tf.float32))
        Y = tf.placeholder((tf.float32))

        W1 = tf.Variable(tf.random_normal([2,2]), name = 'weight1')
        b1 = tf.Variable(tf.random_normal([2]), name = 'bias1')
        layer1 = tf.sigmoid(tf.matmul(X, W1) + b1)

        W2 = tf.Variable(tf.random_normal([2,2]), name = 'weight2')
        b2 = tf.Variable(tf.random_normal([2]), name = 'bias2')
        layer2 = tf.sigmoid(tf.matmul(layer1, W2 ) + b2)

        hypothesis = layer2

        cost = -tf.reduce_mean(Y*tf.log(hypothesis) + (1 - Y)*tf.log(1 - hypothesis))
        train = tf.train.AdamOptimizer(learning_rate = 0.1).minimize(cost)

        # Accuracy
        predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
        accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))
        saver = tf.train.Saver()
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            for step in range(10001):
                sess.run(train, feed_dict = {X: x_data, Y: y_data})
                if step % 1000 == 0:
                    model_path = "./model/model_%d.ckpt" % step
                    save_path = saver.save(sess, model_path)
                if step % 100 == 0:
                    print(step,sess.run(cost,feed_dict={X: x_data, Y: y_data}),sess.run([W1,W2]))

            h, c, a = sess.run([hypothesis, predicted, accuracy], feed_dict={X: x_data, Y: y_data})
            print("\nHypothesis: ", h, "\nCorrect: ", c, "\nAccuracy: ", a)

        sess = tf.Session()
        saver = tf.train.Saver()
        step = 6000
        model_path = "model/model_%d.ckpt" % step
        saver.restore(sess,model_path)
        print("cost: ", sess.run(W1))

# Save model
    # 保存训练好的模型的代码如下：sess = tf.Session()
    saver = tf.train.Saver()  
    model_path = "D:\sample\model.ckpt"
    save_path = saver.save(sess, model_path)
    # 使用时，代码如下:saver = tf.train.Saver()
    saver.restore(sess, "D:\sample\model.ckpt")
    result = sess.run(y, feed_dict={x: data})
