_base_ = './queryinst_r50_fpn_300_proposals_crop_mstrain_480-800_3x_coco.py'

model = dict(
    backbone=dict(
        depth=101,
        init_cfg=dict(type='Pretrained',
                      checkpoint='torchvision://resnet101')))
dataset_type = 'MyDataset'
data_root = 'data/mydataset/'



data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2,
    train=dict(
        type=dataset_type,
        ann_file=data_root + 'annotations/train.json',
        img_prefix=data_root + 'train/',
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        ann_file=data_root + 'annotations/val.json',
        img_prefix=data_root + 'val/',
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        ann_file=data_root + 'annotations/val.json',
        img_prefix=data_root + 'val/',
        pipeline=test_pipeline))

evaluation = dict(interval=400,metric=['bbox', 'segm']) 
runner = dict(type='IterBasedRunner', max_iters=30000)
checkpoint_config = dict(by_epoch=False, interval=800) 

 
work_dir='/hpctmp/pyni/traininglog/'

