import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000

# Options and Output Report
process.options = cms.untracked.PSet(
	wantSummary = cms.untracked.bool(True)
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

import FWCore.Utilities.FileUtils as FileUtils
readFiles = cms.untracked.vstring(FileUtils.loadListFromFile('WplusTo2JWminusToLNuJJ_EWK_LO_aQGC_MJJ100PTJ10_TuneCUETP8M1_13TeV.txt'))
#readFiles = cms.untracked.vstring(FileUtils.loadListFromFile('TEMP_NAME.txt'))


process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    #fileNames = cms.untracked.vstring(
	##'file:/afs/cern.ch/user/r/rasharma/work/aQGC_Studies/MC_SampleGeneration/analyzeLHE/CMSSW_8_0_11/src/GenAnalyzer_Arun/genAnalyzer/test/SMP-RunIISummer15wmLHEGS-00029_142.root'
	#	),
    fileNames = readFiles,
    skipBadFiles = cms.untracked.bool(True)
)


process.demo = cms.EDAnalyzer('GenAnalyzer',
	Verbose		=	cms.bool(False),
	genParticlesInputTag  = cms.InputTag("prunedGenParticles"),	# Uncomment if running on MiniAOD
	#LHEEventInputTag = cms.InputTag("source"),			# Uncomment if running on MiniAOD
	#genParticlesInputTag  = cms.InputTag("genParticles"),		# Uncomment if running on GEN only sample
	LHEEventInputTag = cms.InputTag("externalLHEProducer"),		# Uncomment if running on GEN only

)

#process.GenAnalyzer = cms.EDProducer("GenAnalyzer",
#)

process.p = cms.Path(process.demo)
