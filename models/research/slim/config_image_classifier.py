

PROJ_DIR='/home/duycuong/PycharmProjects/research_py3/tensorflow_slim'
DATASET_NAME='getty_dataset_02'
DATASET_DIR=PROJ_DIR+'/data/'+DATASET_NAME
MODEL_NAME='mobilenet_v1' #inception_v3  #mobilenet_v1
NUM_THREAD=8
input_size=224
resume_dir='/home/duycuong/PycharmProjects/research_py3/tensorflow_slim/train_logs/mobilenet_v1_224_getty_dataset_02/2019-08-23_21.14'
batch_size=32
quant_delay=1

#training
save_ckpt_every_seconds=300
log_every_n_steps=100
MAXIMUM_STEPS=600000

#export inference graph
output_graph='../../../outputs/mobilenet_qt_v1_224_9000.pb'
checkpoint='../../../outputs/2019-08-23_18.06_quant_500000_steps_90_from_scratch/model.ckpt-500000'
output_file='../../../outputs/mobilenet_v1_qt_224_9000_with_ckpt.pb'


CHECKPOINT=''
CHECKPOINT_EXCLUDE=''
TRAINABLE_SCOPE=''
finetune=True
if(finetune and quant_delay==-1):
    if(MODEL_NAME=='inception_v3'):
        CHECKPOINT='/home/atsg/PycharmProjects/gvh205_py3/tensorflow_slim/models/downloaded/inception_v3/inception_v3.ckpt'
        CHECKPOINT_EXCLUDE='InceptionV3/Logits,InceptionV3/AuxLogits' #MobilenetV1
        TRAINABLE_SCOPE='InceptionV3/Logits,InceptionV3/AuxLogits'
    if(MODEL_NAME=='mobilenet_v1'):
        CHECKPOINT='../../downloaded/mobilenet_v1_1.0_224/mobilenet_v1_1.0_224.ckpt'
        CHECKPOINT_EXCLUDE='MobilenetV1/Logits' #MobilenetV1
        #TRAINABLE_SCOPE='MobilenetV1/Logits'