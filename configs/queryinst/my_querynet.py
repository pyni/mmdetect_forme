_base_ = './queryinst_r50_fpn_300_proposals_crop_mstrain_480-800_3x_coco.py'

model = dict(
    backbone=dict(
        depth=101,
        init_cfg=dict(type='Pretrained',
                      checkpoint='torchvision://resnet101')))
 
runner = dict(type='IterBasedRunner', max_iters=30000)
checkpoint_config = dict(by_epoch=False, interval=800) 
 
work_dir='/hpctmp/pyni/traininglog/'

