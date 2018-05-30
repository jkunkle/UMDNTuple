
import os
from argparse import ArgumentParser

p = ArgumentParser()

p.add_argument('--version', dest='version', required=True, help='version' )

options = p.parse_args()

data_samples = [ 
    #'/SingleElectron/Run2016B-23Sep2016-v2/MINIAOD',
    #'/SingleElectron/Run2016B-23Sep2016-v3/MINIAOD',
    #'/SingleElectron/Run2016C-23Sep2016-v1/MINIAOD',
    #'/SingleElectron/Run2016D-23Sep2016-v1/MINIAOD',
    #'/SingleElectron/Run2016E-23Sep2016-v1/MINIAOD',
    #'/SingleElectron/Run2016F-23Sep2016-v1/MINIAOD',
    #'/SingleElectron/Run2016G-23Sep2016-v1/MINIAOD',
    #'/SingleElectron/Run2016H-PromptReco-v1/MINIAOD',
    #'/SingleElectron/Run2016H-PromptReco-v2/MINIAOD',
    #'/SingleElectron/Run2016H-PromptReco-v3/MINIAOD',
    #'/SingleMuon/Run2016B-23Sep2016-v1/MINIAOD',
    #'/SingleMuon/Run2016B-23Sep2016-v3/MINIAOD',
    #'/SingleMuon/Run2016C-23Sep2016-v1/MINIAOD',
    #'/SingleMuon/Run2016D-23Sep2016-v1/MINIAOD',
    #'/SingleMuon/Run2016E-23Sep2016-v1/MINIAOD',
    #'/SingleMuon/Run2016F-23Sep2016-v1/MINIAOD',
    #'/SingleMuon/Run2016G-23Sep2016-v1/MINIAOD',
    #'/SingleMuon/Run2016H-PromptReco-v1/MINIAOD',
    #'/SingleMuon/Run2016H-PromptReco-v2/MINIAOD',
    #'/SingleMuon/Run2016H-PromptReco-v3/MINIAOD',
]

mc_samples = [
    ##('/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/MINIAODSIM', False ),
    #('/DiPhotonJets_MGG-80toInf_13TeV_amcatnloFXFX_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    ##('/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ##('/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ##('/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ##('/GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ##('/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    #('/MadGraphChargedResonance_WGToLNu_M1000_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M1000_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M1200_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M1200_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M1400_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M1400_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M1600_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M1600_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M1800_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M1800_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M2000_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M2000_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M200_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M200_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M2200_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M2200_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M2400_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M2400_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M250_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M250_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M2600_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M2600_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M2800_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M2800_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M3000_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M300_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M300_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M3500_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M3500_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M350_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M350_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M4000_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M4000_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M400_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M400_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M450_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M450_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M500_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M500_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M600_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M600_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M700_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M700_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M800_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M800_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M900_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/MadGraphChargedResonance_WGToLNu_M900_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    ('/PythiaChargedResonance_WGToLNu_M1000_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M1000_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M1200_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M1200_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M1400_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M1400_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M1600_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M1600_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M1800_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M1800_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M2000_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M2000_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M200_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M200_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M2200_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M2200_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M2400_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M2400_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M250_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M250_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M2600_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M2600_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M2800_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M2800_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M3000_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M3000_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M300_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M300_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M3500_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M3500_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M350_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M4000_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M4000_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M400_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M400_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M450_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M450_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M500_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M500_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M600_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M600_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M700_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M700_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M800_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M800_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M900_width0p01/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ('/PythiaChargedResonance_WGToLNu_M900_width5/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    #('/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    ##('/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ##('/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ##('/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM', False ),
    #('/WGToLNuG_PtG-130_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/WGToLNuG_PtG-130_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/WGToLNuG_PtG-500_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/WGToLNuG_PtG-500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM', True ),
    #('/WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    ##('/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ##('/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ##('/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ##('/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ##('/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ##('/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    ##('/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    #('/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    ##('/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    #('/WWG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM', True ),
    ##('/WWTo2L2Nu_13TeV-powheg/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', False ),
    #('/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM', True ),
    #('/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM', True ),
]

json_path = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'

config_dir = 'crab_configs'

if not os.path.isdir( config_dir ) :
    os.mkdir(config_dir ) 

submit_commands = []

for path in data_samples : 

    base_name = path.split('/')[1]+'_'+path.split('/')[2]

    fname = '%s/%s.py'%(config_dir, base_name)

    ofile = open(fname, 'w' )

    file_entries = []

    file_entries.append( 'from CRABClient.UserUtilities import config' )
    file_entries.append( 'config = config()' )
    file_entries.append( '' )
    file_entries.append( 'config.General.requestName = "production_%s_%s"' %( options.version, base_name ) )
    file_entries.append( 'config.General.workArea = "crab_projects" ' )
    file_entries.append( 'config.General.transferOutputs = True' )
    file_entries.append( 'config.General.transferLogs = False' )
    file_entries.append( '' )
    file_entries.append( 'config.JobType.pluginName = "Analysis"' )
    file_entries.append( 'config.JobType.psetName = "run_production_cfg.py"' )
    file_entries.append( 'config.JobType.pyCfgParams = ["isMC=0"]' )
    file_entries.append( '' )
    file_entries.append( 'config.Data.inputDataset = "%s"' %path )
    file_entries.append( 'config.Data.splitting = "LumiBased"' )
    file_entries.append( 'config.Data.unitsPerJob = 300' )
    file_entries.append( 'config.Data.outLFNDirBase = "/store/user/jkunkle/"' )
    file_entries.append( 'config.Data.publication = False' )
    file_entries.append( 'config.Data.outputDatasetTag = "UMDNTuple_%s"' %options.version )
    file_entries.append( 'config.Data.lumiMask = "%s"' %json_path)
    file_entries.append( '' )
    file_entries.append( 'config.Site.storageSite = "T3_US_UMD"' )

    for line in file_entries : 
        ofile.write( line + '\n' )

    ofile.close()

    submit_commands.append( 'crab submit --config %s' %( fname ) )

                       



for path, useEventWeights in mc_samples: 

    base_name = path.split('/')[1]

    fname = '%s/%s.py'%(config_dir, base_name)

    ofile = open(fname, 'w' )

    file_entries = []

    file_entries.append('from CRABClient.UserUtilities import config')
    file_entries.append('config = config()')
    file_entries.append('config.General.workArea = "crab_projects"')
    file_entries.append('config.General.transferOutputs = True')
    file_entries.append('config.General.transferLogs = False')
    file_entries.append('config.JobType.pluginName = "Analysis"')
    file_entries.append('config.JobType.psetName = "run_production_cfg.py"')
    file_entries.append('config.Data.outLFNDirBase = "/store/user/jkunkle/"')
    file_entries.append('config.Data.publication = False')
    file_entries.append('config.Site.storageSite = "T3_US_UMD"')
    file_entries.append('config.Data.outputDatasetTag= "UMDNTuple_%s"' %options.version)
    file_entries.append('config.JobType.pyCfgParams = ["isMC=1", "disableEventWeights=%d"]' %(not useEventWeights))
    file_entries.append('config.General.requestName = "production_%s_%s"' %(options.version, base_name))
    file_entries.append('config.Data.inputDataset = "%s"' %path)
    file_entries.append('config.Data.splitting = "FileBased"')
    file_entries.append('config.Data.unitsPerJob = 10')

    for line in file_entries : 
        ofile.write( line + '\n' )

    ofile.close()

    submit_commands.append( 'crab submit --config %s' %( fname ) )

submit_file = open('submit_crab.csh', 'w' )

submit_file.write( '#!/bin/tcsh\n' )
submit_file.write( 'cmsenv\n' )
submit_file.write( 'source /cvmfs/cms.cern.ch/crab3/crab.csh\n' )

for cmd in submit_commands :
    submit_file.write(cmd + '\n' )


submit_file.close()

                       




