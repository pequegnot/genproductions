import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2Settings_cfi import *

generator = cms.EDFilter('Pythia6GeneratorFilter',
	comEnergy = cms.double(8000.0),
	crossSection = cms.untracked.double(1.22644324437e+6),
	filterEfficiency = cms.untracked.double(0.55),
	maxEventsToPrint = cms.untracked.int32(0),
	pythiaHepMCVerbosity = cms.untracked.bool(False),
	pythiaPylistVerbosity = cms.untracked.int32(0),

	PythiaParameters = cms.PSet(
		pythiaUESettingsBlock,
		processParameters = cms.vstring(
			'MSEL = 1        ! QCD hight pT processes',
			'CKIN(3) = 80    ! minimum pt hat for hard interactions',
                        'CKIN(4) = 170   ! maximum pt hat for hard interactions',
		),
		parameterSets = cms.vstring(
			'pythiaUESettings',
			'processParameters',
		)
	)
)

configurationMetadata = cms.untracked.PSet(
	version = cms.untracked.string('\$Revision: 1.1 $'),
	name = cms.untracked.string('\$Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/GenProduction/python/QCD_Pt_80to170_6GenJets_TuneZ2_8TeV_pythia6_cff.py,v $'),
	annotation = cms.untracked.string('Spring2011 sample with PYTHIA6: QCD multijet production, 80 GeV < pThat < 170 GeV , >= 6 ak5GenJets (pt > 15, |eta| < 3) , TuneZ2')
)

from PhysicsTools.HepMCCandAlgos.genParticles_cfi import genParticles
from RecoJets.Configuration.GenJetParticles_cff import genParticlesForJets
from RecoJets.JetProducers.ak5GenJets_cfi import ak5GenJets

genJetSelector = cms.EDFilter("CandViewSelector",
                              src = cms.InputTag("ak5GenJets"),
                              cut = cms.string("pt > 15 & abs(eta) < 3.0")
                              )

genJetFilter = cms.EDFilter("CandViewCountFilter",
                            src = cms.InputTag("genJetSelector"),
                            minNumber = cms.uint32(6)
                            )

ProductionFilterSequence = cms.Sequence(generator*genParticles*genParticlesForJets*ak5GenJets*genJetSelector*genJetFilter)

