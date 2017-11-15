### Dumps 介绍
``` zsh
9242/9242 [==============================] - 42s - loss: 0.1404 - acc: 0.9619 - val_loss: 1.7997 - val_acc: 0.6972
# 目前, 模型的 .fit() 中有下列参数会被记录到 logs 中:
# 在每个 epoch 的结尾处 (on_epoch_end)，logs 将包含训练的正确率和误差, acc 和 loss,
#     如果指定了验证集; 还会包含验证集正确率和误差 val_acc 和 val_loss, val_acc 还额外需要在 .compile 中启用 metrics=['accuracy']
# 在每个 batch 的开始处 (on_batch_begin), logs 包含 size, 即当前 batch 的样本数
# 在每个 batch 的结尾处 (on_batch_end), logs 包含 loss, 若启用 accuracy 则还包含 acc
```
