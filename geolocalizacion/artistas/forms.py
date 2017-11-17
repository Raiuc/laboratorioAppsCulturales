# coding=utf-8
from django import forms

class FormaImportacion(forms.Form):
    """
    Form for SynchBatch & SkuSynch data import
    """
    excel                = forms.FileField(required=True)
    num_registers        = forms.IntegerField(required=True)
    num_skus             = forms.IntegerField(required=True)

    customer             = forms.CharField(required=True)
    description          = forms.CharField(required=True)
    cedis                = forms.CharField(required=False)
    num_cedis            = forms.IntegerField(required=True)
    ordering             = forms.CharField(required=False)

    # schedule (Commented until Internationalization)
    # sb.pres_tx1         = request.POST['pres_tx1']
    # sb.pres_tx2         = request.POST['pres_tx2']
    # sb.pres_tx3         = request.POST['pres_tx3']

    ## Start
    start_period         = forms.CharField(required=True)
    start_title          = forms.CharField(required=True)
    start_tx0            = forms.CharField(required=True)
    start_tx1            = forms.CharField(required=False)
    start_tx2            = forms.CharField(required=False)
    start_tx3            = forms.CharField(required=False)
    start_tx4            = forms.CharField(required=False)
    ## Presentation (start) images
    pres_img1            = forms.FileField(required=False)
    pres_img2            = forms.FileField(required=False)
    pres_img3            = forms.FileField(required=False)
    inter_tx0            = forms.CharField(required=False)
    inter_tx1            = forms.CharField(required=False)
    inter_tx2            = forms.CharField(required=False)
    inter_tx3            = forms.CharField(required=False)
    inter_tx4            = forms.CharField(required=False)

    ## Achievements
    achiev_title        = forms.CharField(required=False)
    achiev_tx0          = forms.CharField(required=False)
    achiev_tx1          = forms.CharField(required=False)
    achiev_tx2          = forms.CharField(required=False)
    achiev_tx3          = forms.CharField(required=False)
    achiev_tx4          = forms.CharField(required=False)

    ## Benchmark
    cus1                = forms.CharField(required=False)
    synch1              = forms.CharField(required=False)
    stock1              = forms.CharField(required=False)
    sales1              = forms.CharField(required=False)
    cus2                = forms.CharField(required=False)
    synch2              = forms.CharField(required=False)
    stock2              = forms.CharField(required=False)
    sales2              = forms.CharField(required=False)
    cus3                = forms.CharField(required=False)
    synch3              = forms.CharField(required=False)
    stock3              = forms.CharField(required=False)
    sales3              = forms.CharField(required=False)
    cus4                = forms.CharField(required=False)
    synch4              = forms.CharField(required=False)
    stock4              = forms.CharField(required=False)
    sales4              = forms.CharField(required=False)
    cus5                = forms.CharField(required=False)
    synch5              = forms.CharField(required=False)
    stock5              = forms.CharField(required=False)
    sales5              = forms.CharField(required=False)
    cus6                = forms.CharField(required=False)
    synch6              = forms.CharField(required=False)
    stock6              = forms.CharField(required=False)
    sales6              = forms.CharField(required=False)
    cus7                = forms.CharField(required=False)
    synch7              = forms.CharField(required=False)
    stock7              = forms.CharField(required=False)
    sales7              = forms.CharField(required=False)

    ## Success stories
    succ1_title         = forms.CharField(required=False)
    succ2_title         = forms.CharField(required=False)
    succ3_title         = forms.CharField(required=False)

    succ1_0_tx          = forms.CharField(required=False)
    succ1_1_tx          = forms.CharField(required=False)
    succ1_2_tx          = forms.CharField(required=False)

    succ2_0_tx          = forms.CharField(required=False)
    succ2_1_tx          = forms.CharField(required=False)
    succ2_2_tx          = forms.CharField(required=False)

    succ3_0_tx          = forms.CharField(required=False)
    succ3_1_tx          = forms.CharField(required=False)
    succ3_2_tx          = forms.CharField(required=False)

    ## Success images
    succ1_img1          = forms.FileField(required=False)
    succ1_img2          = forms.FileField(required=False)
    succ1_img3          = forms.FileField(required=False)
    succ2_img1          = forms.FileField(required=False)
    succ2_img2          = forms.FileField(required=False)
    succ2_img3          = forms.FileField(required=False)
    succ3_img1          = forms.FileField(required=False)
    succ3_img2          = forms.FileField(required=False)
    succ3_img3          = forms.FileField(required=False)

    ## Incremental sales (Simulator)
    increm1_tx          = forms.CharField(required=False)
    increm1_amount      = forms.IntegerField(required=False)
    increm2_tx          = forms.CharField(required=False)
    increm2_amount      = forms.IntegerField(required=False)
    increm3_tx          = forms.CharField(required=False)
    increm3_amount      = forms.IntegerField(required=False)

    increm1_img1        = forms.FileField(required=False)
    increm1_img2        = forms.FileField(required=False)
    increm1_img3        = forms.FileField(required=False)

    increm2_img1        = forms.FileField(required=False)
    increm2_img2        = forms.FileField(required=False)
    increm2_img3        = forms.FileField(required=False)

    increm3_img1        = forms.FileField(required=False)
    increm3_img2        = forms.FileField(required=False)
    increm3_img3        = forms.FileField(required=False)

    # Lead time & Replenishment Interval (Simulator)
    agility0            = forms.IntegerField(required=True)
    agility1            = forms.IntegerField(required=True)
    agility2            = forms.IntegerField(required=True)
    agility3            = forms.IntegerField(required=True)
    agility4            = forms.IntegerField(required=True)
    agility5            = forms.IntegerField(required=True)
    agility6            = forms.IntegerField(required=True)
    agility7            = forms.IntegerField(required=True)
    agility8            = forms.IntegerField(required=True)
    reple_time          = forms.IntegerField(required=True)
