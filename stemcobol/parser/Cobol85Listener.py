# Generated from Cobol85.g4 by ANTLR 4.7.1
from antlr4 import *

import copy
import logging
from functools import partial
import stemtree

# NOTE: kernel can be placed on the levels of statement, sentence, paragraph, or section.
#       However, the begin and end of kernel should match the same level each other. 

# This class defines a complete listener for a parse tree produced by Cobol85Parser.
class Cobol85Listener(ParseTreeListener):

    def __init__(self, root, stream):
        self.root = root
        self.stream = stream
        self._stack = [root]

        for i in range(len(self.stream.tokens)):
            token = self.stream.tokens[i]
            if token.channel != token.HIDDEN_CHANNEL:
                break
            cnode = self.root.__class__()
            cnode.name = 'hidden'
            cnode.text = token.text
            cnode.token = token.type
            cnode.uppernode = root
            cnode.root = root
            root.add_subnode(cnode)

    #def visitTerminal(self, node:TerminalNode):
    def visitTerminal(self, node):

        uppernode = self._stack[-1]

        tnode = self.root.__class__()
        tnode.name = 'terminal'
        tnode.text = node.symbol.text
        tnode.token = node.symbol.type
        tnode.uppernode = uppernode
        tnode.root = self.root
        uppernode.add_subnode(tnode)

        for i in range(node.symbol.tokenIndex+1, len(self.stream.tokens)):
            token = self.stream.tokens[i]
            if token.channel != token.HIDDEN_CHANNEL:
                break
            cnode = self.root.__class__()
            cnode.name = 'hidden'
            cnode.text = token.text
            cnode.token = token.type
            cnode.uppernode = uppernode
            cnode.root = self.root
            uppernode.add_subnode(cnode)

    def pop_stack(self, name, ctx):

        self._stack.pop()

    def add_node(self, name, ctx):

        uppernode = self._stack[-1]

        node = self.root.__class__()
        node.name = name[5:]
        node.uppernode = uppernode
        node.root = self.root
        uppernode.add_subnode(node)

        self._stack.append(node)

    def __getattr__(self, name):
        if name.startswith('enter'):
            return partial(self.add_node, name)
        elif name.startswith('exit'):
            return partial(self.pop_stack, name)
        else:
            import pdb; pdb.set_trace()

#    # Enter a parse tree produced by Cobol85Parser#startRule.
#    def enterStartRule(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#startRule.
#    def exitStartRule(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#compilationUnit.
#    def enterCompilationUnit(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#compilationUnit.
#    def exitCompilationUnit(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#programUnit.
#    def enterProgramUnit(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#programUnit.
#    def exitProgramUnit(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#endProgramStatement.
#    def enterEndProgramStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#endProgramStatement.
#    def exitEndProgramStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#identificationDivision.
#    def enterIdentificationDivision(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#identificationDivision.
#    def exitIdentificationDivision(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#identificationDivisionBody.
#    def enterIdentificationDivisionBody(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#identificationDivisionBody.
#    def exitIdentificationDivisionBody(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#programIdParagraph.
#    def enterProgramIdParagraph(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#programIdParagraph.
#    def exitProgramIdParagraph(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#authorParagraph.
#    def enterAuthorParagraph(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#authorParagraph.
#    def exitAuthorParagraph(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#installationParagraph.
#    def enterInstallationParagraph(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#installationParagraph.
#    def exitInstallationParagraph(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dateWrittenParagraph.
#    def enterDateWrittenParagraph(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dateWrittenParagraph.
#    def exitDateWrittenParagraph(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dateCompiledParagraph.
#    def enterDateCompiledParagraph(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dateCompiledParagraph.
#    def exitDateCompiledParagraph(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#securityParagraph.
#    def enterSecurityParagraph(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#securityParagraph.
#    def exitSecurityParagraph(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#remarksParagraph.
#    def enterRemarksParagraph(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#remarksParagraph.
#    def exitRemarksParagraph(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#environmentDivision.
#    def enterEnvironmentDivision(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#environmentDivision.
#    def exitEnvironmentDivision(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#environmentDivisionBody.
#    def enterEnvironmentDivisionBody(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#environmentDivisionBody.
#    def exitEnvironmentDivisionBody(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#configurationSection.
#    def enterConfigurationSection(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#configurationSection.
#    def exitConfigurationSection(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#configurationSectionParagraph.
#    def enterConfigurationSectionParagraph(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#configurationSectionParagraph.
#    def exitConfigurationSectionParagraph(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sourceComputerParagraph.
#    def enterSourceComputerParagraph(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sourceComputerParagraph.
#    def exitSourceComputerParagraph(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#objectComputerParagraph.
#    def enterObjectComputerParagraph(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#objectComputerParagraph.
#    def exitObjectComputerParagraph(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#objectComputerClause.
#    def enterObjectComputerClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#objectComputerClause.
#    def exitObjectComputerClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#memorySizeClause.
#    def enterMemorySizeClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#memorySizeClause.
#    def exitMemorySizeClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#diskSizeClause.
#    def enterDiskSizeClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#diskSizeClause.
#    def exitDiskSizeClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#collatingSequenceClause.
#    def enterCollatingSequenceClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#collatingSequenceClause.
#    def exitCollatingSequenceClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#collatingSequenceClauseAlphanumeric.
#    def enterCollatingSequenceClauseAlphanumeric(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#collatingSequenceClauseAlphanumeric.
#    def exitCollatingSequenceClauseAlphanumeric(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#collatingSequenceClauseNational.
#    def enterCollatingSequenceClauseNational(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#collatingSequenceClauseNational.
#    def exitCollatingSequenceClauseNational(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#segmentLimitClause.
#    def enterSegmentLimitClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#segmentLimitClause.
#    def exitSegmentLimitClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#characterSetClause.
#    def enterCharacterSetClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#characterSetClause.
#    def exitCharacterSetClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#specialNamesParagraph.
#    def enterSpecialNamesParagraph(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#specialNamesParagraph.
#    def exitSpecialNamesParagraph(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#specialNameClause.
#    def enterSpecialNameClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#specialNameClause.
#    def exitSpecialNameClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#alphabetClause.
#    def enterAlphabetClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#alphabetClause.
#    def exitAlphabetClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#alphabetClauseFormat1.
#    def enterAlphabetClauseFormat1(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#alphabetClauseFormat1.
#    def exitAlphabetClauseFormat1(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#alphabetLiterals.
#    def enterAlphabetLiterals(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#alphabetLiterals.
#    def exitAlphabetLiterals(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#alphabetThrough.
#    def enterAlphabetThrough(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#alphabetThrough.
#    def exitAlphabetThrough(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#alphabetAlso.
#    def enterAlphabetAlso(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#alphabetAlso.
#    def exitAlphabetAlso(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#alphabetClauseFormat2.
#    def enterAlphabetClauseFormat2(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#alphabetClauseFormat2.
#    def exitAlphabetClauseFormat2(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#channelClause.
#    def enterChannelClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#channelClause.
#    def exitChannelClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#classClause.
#    def enterClassClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#classClause.
#    def exitClassClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#classClauseThrough.
#    def enterClassClauseThrough(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#classClauseThrough.
#    def exitClassClauseThrough(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#classClauseFrom.
#    def enterClassClauseFrom(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#classClauseFrom.
#    def exitClassClauseFrom(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#classClauseTo.
#    def enterClassClauseTo(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#classClauseTo.
#    def exitClassClauseTo(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#currencySignClause.
#    def enterCurrencySignClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#currencySignClause.
#    def exitCurrencySignClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#decimalPointClause.
#    def enterDecimalPointClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#decimalPointClause.
#    def exitDecimalPointClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#defaultComputationalSignClause.
#    def enterDefaultComputationalSignClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#defaultComputationalSignClause.
#    def exitDefaultComputationalSignClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#defaultDisplaySignClause.
#    def enterDefaultDisplaySignClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#defaultDisplaySignClause.
#    def exitDefaultDisplaySignClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#environmentSwitchNameClause.
#    def enterEnvironmentSwitchNameClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#environmentSwitchNameClause.
#    def exitEnvironmentSwitchNameClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#environmentSwitchNameSpecialNamesStatusPhrase.
#    def enterEnvironmentSwitchNameSpecialNamesStatusPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#environmentSwitchNameSpecialNamesStatusPhrase.
#    def exitEnvironmentSwitchNameSpecialNamesStatusPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#odtClause.
#    def enterOdtClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#odtClause.
#    def exitOdtClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reserveNetworkClause.
#    def enterReserveNetworkClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reserveNetworkClause.
#    def exitReserveNetworkClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#symbolicCharactersClause.
#    def enterSymbolicCharactersClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#symbolicCharactersClause.
#    def exitSymbolicCharactersClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#symbolicCharacters.
#    def enterSymbolicCharacters(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#symbolicCharacters.
#    def exitSymbolicCharacters(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#inputOutputSection.
#    def enterInputOutputSection(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#inputOutputSection.
#    def exitInputOutputSection(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#inputOutputSectionParagraph.
#    def enterInputOutputSectionParagraph(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#inputOutputSectionParagraph.
#    def exitInputOutputSectionParagraph(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#fileControlParagraph.
#    def enterFileControlParagraph(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#fileControlParagraph.
#    def exitFileControlParagraph(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#fileControlEntry.
#    def enterFileControlEntry(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#fileControlEntry.
#    def exitFileControlEntry(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#selectClause.
#    def enterSelectClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#selectClause.
#    def exitSelectClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#fileControlClause.
#    def enterFileControlClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#fileControlClause.
#    def exitFileControlClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#assignClause.
#    def enterAssignClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#assignClause.
#    def exitAssignClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reserveClause.
#    def enterReserveClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reserveClause.
#    def exitReserveClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#organizationClause.
#    def enterOrganizationClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#organizationClause.
#    def exitOrganizationClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#paddingCharacterClause.
#    def enterPaddingCharacterClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#paddingCharacterClause.
#    def exitPaddingCharacterClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#recordDelimiterClause.
#    def enterRecordDelimiterClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#recordDelimiterClause.
#    def exitRecordDelimiterClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#accessModeClause.
#    def enterAccessModeClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#accessModeClause.
#    def exitAccessModeClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#recordKeyClause.
#    def enterRecordKeyClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#recordKeyClause.
#    def exitRecordKeyClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#alternateRecordKeyClause.
#    def enterAlternateRecordKeyClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#alternateRecordKeyClause.
#    def exitAlternateRecordKeyClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#passwordClause.
#    def enterPasswordClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#passwordClause.
#    def exitPasswordClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#fileStatusClause.
#    def enterFileStatusClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#fileStatusClause.
#    def exitFileStatusClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#relativeKeyClause.
#    def enterRelativeKeyClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#relativeKeyClause.
#    def exitRelativeKeyClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#ioControlParagraph.
#    def enterIoControlParagraph(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#ioControlParagraph.
#    def exitIoControlParagraph(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#ioControlClause.
#    def enterIoControlClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#ioControlClause.
#    def exitIoControlClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#rerunClause.
#    def enterRerunClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#rerunClause.
#    def exitRerunClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#rerunEveryRecords.
#    def enterRerunEveryRecords(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#rerunEveryRecords.
#    def exitRerunEveryRecords(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#rerunEveryOf.
#    def enterRerunEveryOf(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#rerunEveryOf.
#    def exitRerunEveryOf(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#rerunEveryClock.
#    def enterRerunEveryClock(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#rerunEveryClock.
#    def exitRerunEveryClock(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sameClause.
#    def enterSameClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sameClause.
#    def exitSameClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#multipleFileClause.
#    def enterMultipleFileClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#multipleFileClause.
#    def exitMultipleFileClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#multipleFilePosition.
#    def enterMultipleFilePosition(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#multipleFilePosition.
#    def exitMultipleFilePosition(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#commitmentControlClause.
#    def enterCommitmentControlClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#commitmentControlClause.
#    def exitCommitmentControlClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataDivision.
#    def enterDataDivision(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataDivision.
#    def exitDataDivision(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataDivisionSection.
#    def enterDataDivisionSection(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataDivisionSection.
#    def exitDataDivisionSection(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#fileSection.
#    def enterFileSection(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#fileSection.
#    def exitFileSection(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#fileDescriptionEntry.
#    def enterFileDescriptionEntry(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#fileDescriptionEntry.
#    def exitFileDescriptionEntry(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#fileDescriptionEntryClause.
#    def enterFileDescriptionEntryClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#fileDescriptionEntryClause.
#    def exitFileDescriptionEntryClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#externalClause.
#    def enterExternalClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#externalClause.
#    def exitExternalClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#globalClause.
#    def enterGlobalClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#globalClause.
#    def exitGlobalClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#blockContainsClause.
#    def enterBlockContainsClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#blockContainsClause.
#    def exitBlockContainsClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#blockContainsTo.
#    def enterBlockContainsTo(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#blockContainsTo.
#    def exitBlockContainsTo(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#recordContainsClause.
#    def enterRecordContainsClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#recordContainsClause.
#    def exitRecordContainsClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#recordContainsClauseFormat1.
#    def enterRecordContainsClauseFormat1(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#recordContainsClauseFormat1.
#    def exitRecordContainsClauseFormat1(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#recordContainsClauseFormat2.
#    def enterRecordContainsClauseFormat2(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#recordContainsClauseFormat2.
#    def exitRecordContainsClauseFormat2(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#recordContainsClauseFormat3.
#    def enterRecordContainsClauseFormat3(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#recordContainsClauseFormat3.
#    def exitRecordContainsClauseFormat3(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#recordContainsTo.
#    def enterRecordContainsTo(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#recordContainsTo.
#    def exitRecordContainsTo(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#labelRecordsClause.
#    def enterLabelRecordsClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#labelRecordsClause.
#    def exitLabelRecordsClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#valueOfClause.
#    def enterValueOfClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#valueOfClause.
#    def exitValueOfClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#valuePair.
#    def enterValuePair(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#valuePair.
#    def exitValuePair(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataRecordsClause.
#    def enterDataRecordsClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataRecordsClause.
#    def exitDataRecordsClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#linageClause.
#    def enterLinageClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#linageClause.
#    def exitLinageClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#linageAt.
#    def enterLinageAt(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#linageAt.
#    def exitLinageAt(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#linageFootingAt.
#    def enterLinageFootingAt(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#linageFootingAt.
#    def exitLinageFootingAt(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#linageLinesAtTop.
#    def enterLinageLinesAtTop(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#linageLinesAtTop.
#    def exitLinageLinesAtTop(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#linageLinesAtBottom.
#    def enterLinageLinesAtBottom(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#linageLinesAtBottom.
#    def exitLinageLinesAtBottom(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#recordingModeClause.
#    def enterRecordingModeClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#recordingModeClause.
#    def exitRecordingModeClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#modeStatement.
#    def enterModeStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#modeStatement.
#    def exitModeStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#codeSetClause.
#    def enterCodeSetClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#codeSetClause.
#    def exitCodeSetClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportClause.
#    def enterReportClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportClause.
#    def exitReportClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataBaseSection.
#    def enterDataBaseSection(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataBaseSection.
#    def exitDataBaseSection(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataBaseSectionEntry.
#    def enterDataBaseSectionEntry(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataBaseSectionEntry.
#    def exitDataBaseSectionEntry(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#workingStorageSection.
#    def enterWorkingStorageSection(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#workingStorageSection.
#    def exitWorkingStorageSection(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#linkageSection.
#    def enterLinkageSection(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#linkageSection.
#    def exitLinkageSection(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#communicationSection.
#    def enterCommunicationSection(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#communicationSection.
#    def exitCommunicationSection(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#communicationDescriptionEntry.
#    def enterCommunicationDescriptionEntry(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#communicationDescriptionEntry.
#    def exitCommunicationDescriptionEntry(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#communicationDescriptionEntryFormat1.
#    def enterCommunicationDescriptionEntryFormat1(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#communicationDescriptionEntryFormat1.
#    def exitCommunicationDescriptionEntryFormat1(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#communicationDescriptionEntryFormat2.
#    def enterCommunicationDescriptionEntryFormat2(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#communicationDescriptionEntryFormat2.
#    def exitCommunicationDescriptionEntryFormat2(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#communicationDescriptionEntryFormat3.
#    def enterCommunicationDescriptionEntryFormat3(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#communicationDescriptionEntryFormat3.
#    def exitCommunicationDescriptionEntryFormat3(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#destinationCountClause.
#    def enterDestinationCountClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#destinationCountClause.
#    def exitDestinationCountClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#destinationTableClause.
#    def enterDestinationTableClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#destinationTableClause.
#    def exitDestinationTableClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#endKeyClause.
#    def enterEndKeyClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#endKeyClause.
#    def exitEndKeyClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#errorKeyClause.
#    def enterErrorKeyClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#errorKeyClause.
#    def exitErrorKeyClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#messageCountClause.
#    def enterMessageCountClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#messageCountClause.
#    def exitMessageCountClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#messageDateClause.
#    def enterMessageDateClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#messageDateClause.
#    def exitMessageDateClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#messageTimeClause.
#    def enterMessageTimeClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#messageTimeClause.
#    def exitMessageTimeClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#statusKeyClause.
#    def enterStatusKeyClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#statusKeyClause.
#    def exitStatusKeyClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#symbolicDestinationClause.
#    def enterSymbolicDestinationClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#symbolicDestinationClause.
#    def exitSymbolicDestinationClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#symbolicQueueClause.
#    def enterSymbolicQueueClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#symbolicQueueClause.
#    def exitSymbolicQueueClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#symbolicSourceClause.
#    def enterSymbolicSourceClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#symbolicSourceClause.
#    def exitSymbolicSourceClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#symbolicTerminalClause.
#    def enterSymbolicTerminalClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#symbolicTerminalClause.
#    def exitSymbolicTerminalClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#symbolicSubQueueClause.
#    def enterSymbolicSubQueueClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#symbolicSubQueueClause.
#    def exitSymbolicSubQueueClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#textLengthClause.
#    def enterTextLengthClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#textLengthClause.
#    def exitTextLengthClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#localStorageSection.
#    def enterLocalStorageSection(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#localStorageSection.
#    def exitLocalStorageSection(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenSection.
#    def enterScreenSection(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenSection.
#    def exitScreenSection(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionEntry.
#    def enterScreenDescriptionEntry(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionEntry.
#    def exitScreenDescriptionEntry(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionBlankClause.
#    def enterScreenDescriptionBlankClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionBlankClause.
#    def exitScreenDescriptionBlankClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionBellClause.
#    def enterScreenDescriptionBellClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionBellClause.
#    def exitScreenDescriptionBellClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionBlinkClause.
#    def enterScreenDescriptionBlinkClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionBlinkClause.
#    def exitScreenDescriptionBlinkClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionEraseClause.
#    def enterScreenDescriptionEraseClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionEraseClause.
#    def exitScreenDescriptionEraseClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionLightClause.
#    def enterScreenDescriptionLightClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionLightClause.
#    def exitScreenDescriptionLightClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionGridClause.
#    def enterScreenDescriptionGridClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionGridClause.
#    def exitScreenDescriptionGridClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionReverseVideoClause.
#    def enterScreenDescriptionReverseVideoClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionReverseVideoClause.
#    def exitScreenDescriptionReverseVideoClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionUnderlineClause.
#    def enterScreenDescriptionUnderlineClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionUnderlineClause.
#    def exitScreenDescriptionUnderlineClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionSizeClause.
#    def enterScreenDescriptionSizeClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionSizeClause.
#    def exitScreenDescriptionSizeClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionLineClause.
#    def enterScreenDescriptionLineClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionLineClause.
#    def exitScreenDescriptionLineClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionColumnClause.
#    def enterScreenDescriptionColumnClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionColumnClause.
#    def exitScreenDescriptionColumnClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionForegroundColorClause.
#    def enterScreenDescriptionForegroundColorClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionForegroundColorClause.
#    def exitScreenDescriptionForegroundColorClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionBackgroundColorClause.
#    def enterScreenDescriptionBackgroundColorClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionBackgroundColorClause.
#    def exitScreenDescriptionBackgroundColorClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionControlClause.
#    def enterScreenDescriptionControlClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionControlClause.
#    def exitScreenDescriptionControlClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionValueClause.
#    def enterScreenDescriptionValueClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionValueClause.
#    def exitScreenDescriptionValueClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionPictureClause.
#    def enterScreenDescriptionPictureClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionPictureClause.
#    def exitScreenDescriptionPictureClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionFromClause.
#    def enterScreenDescriptionFromClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionFromClause.
#    def exitScreenDescriptionFromClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionToClause.
#    def enterScreenDescriptionToClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionToClause.
#    def exitScreenDescriptionToClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionUsingClause.
#    def enterScreenDescriptionUsingClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionUsingClause.
#    def exitScreenDescriptionUsingClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionUsageClause.
#    def enterScreenDescriptionUsageClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionUsageClause.
#    def exitScreenDescriptionUsageClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionBlankWhenZeroClause.
#    def enterScreenDescriptionBlankWhenZeroClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionBlankWhenZeroClause.
#    def exitScreenDescriptionBlankWhenZeroClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionJustifiedClause.
#    def enterScreenDescriptionJustifiedClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionJustifiedClause.
#    def exitScreenDescriptionJustifiedClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionSignClause.
#    def enterScreenDescriptionSignClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionSignClause.
#    def exitScreenDescriptionSignClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionAutoClause.
#    def enterScreenDescriptionAutoClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionAutoClause.
#    def exitScreenDescriptionAutoClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionSecureClause.
#    def enterScreenDescriptionSecureClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionSecureClause.
#    def exitScreenDescriptionSecureClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionRequiredClause.
#    def enterScreenDescriptionRequiredClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionRequiredClause.
#    def exitScreenDescriptionRequiredClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionPromptClause.
#    def enterScreenDescriptionPromptClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionPromptClause.
#    def exitScreenDescriptionPromptClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionPromptOccursClause.
#    def enterScreenDescriptionPromptOccursClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionPromptOccursClause.
#    def exitScreenDescriptionPromptOccursClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionFullClause.
#    def enterScreenDescriptionFullClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionFullClause.
#    def exitScreenDescriptionFullClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenDescriptionZeroFillClause.
#    def enterScreenDescriptionZeroFillClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenDescriptionZeroFillClause.
#    def exitScreenDescriptionZeroFillClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportSection.
#    def enterReportSection(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportSection.
#    def exitReportSection(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportDescription.
#    def enterReportDescription(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportDescription.
#    def exitReportDescription(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportDescriptionEntry.
#    def enterReportDescriptionEntry(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportDescriptionEntry.
#    def exitReportDescriptionEntry(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportDescriptionGlobalClause.
#    def enterReportDescriptionGlobalClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportDescriptionGlobalClause.
#    def exitReportDescriptionGlobalClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportDescriptionPageLimitClause.
#    def enterReportDescriptionPageLimitClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportDescriptionPageLimitClause.
#    def exitReportDescriptionPageLimitClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportDescriptionHeadingClause.
#    def enterReportDescriptionHeadingClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportDescriptionHeadingClause.
#    def exitReportDescriptionHeadingClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportDescriptionFirstDetailClause.
#    def enterReportDescriptionFirstDetailClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportDescriptionFirstDetailClause.
#    def exitReportDescriptionFirstDetailClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportDescriptionLastDetailClause.
#    def enterReportDescriptionLastDetailClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportDescriptionLastDetailClause.
#    def exitReportDescriptionLastDetailClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportDescriptionFootingClause.
#    def enterReportDescriptionFootingClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportDescriptionFootingClause.
#    def exitReportDescriptionFootingClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupDescriptionEntry.
#    def enterReportGroupDescriptionEntry(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupDescriptionEntry.
#    def exitReportGroupDescriptionEntry(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupDescriptionEntryFormat1.
#    def enterReportGroupDescriptionEntryFormat1(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupDescriptionEntryFormat1.
#    def exitReportGroupDescriptionEntryFormat1(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupDescriptionEntryFormat2.
#    def enterReportGroupDescriptionEntryFormat2(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupDescriptionEntryFormat2.
#    def exitReportGroupDescriptionEntryFormat2(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupDescriptionEntryFormat3.
#    def enterReportGroupDescriptionEntryFormat3(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupDescriptionEntryFormat3.
#    def exitReportGroupDescriptionEntryFormat3(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupBlankWhenZeroClause.
#    def enterReportGroupBlankWhenZeroClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupBlankWhenZeroClause.
#    def exitReportGroupBlankWhenZeroClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupColumnNumberClause.
#    def enterReportGroupColumnNumberClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupColumnNumberClause.
#    def exitReportGroupColumnNumberClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupIndicateClause.
#    def enterReportGroupIndicateClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupIndicateClause.
#    def exitReportGroupIndicateClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupJustifiedClause.
#    def enterReportGroupJustifiedClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupJustifiedClause.
#    def exitReportGroupJustifiedClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupLineNumberClause.
#    def enterReportGroupLineNumberClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupLineNumberClause.
#    def exitReportGroupLineNumberClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupLineNumberNextPage.
#    def enterReportGroupLineNumberNextPage(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupLineNumberNextPage.
#    def exitReportGroupLineNumberNextPage(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupLineNumberPlus.
#    def enterReportGroupLineNumberPlus(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupLineNumberPlus.
#    def exitReportGroupLineNumberPlus(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupNextGroupClause.
#    def enterReportGroupNextGroupClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupNextGroupClause.
#    def exitReportGroupNextGroupClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupNextGroupPlus.
#    def enterReportGroupNextGroupPlus(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupNextGroupPlus.
#    def exitReportGroupNextGroupPlus(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupNextGroupNextPage.
#    def enterReportGroupNextGroupNextPage(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupNextGroupNextPage.
#    def exitReportGroupNextGroupNextPage(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupPictureClause.
#    def enterReportGroupPictureClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupPictureClause.
#    def exitReportGroupPictureClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupResetClause.
#    def enterReportGroupResetClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupResetClause.
#    def exitReportGroupResetClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupSignClause.
#    def enterReportGroupSignClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupSignClause.
#    def exitReportGroupSignClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupSourceClause.
#    def enterReportGroupSourceClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupSourceClause.
#    def exitReportGroupSourceClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupSumClause.
#    def enterReportGroupSumClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupSumClause.
#    def exitReportGroupSumClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupTypeClause.
#    def enterReportGroupTypeClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupTypeClause.
#    def exitReportGroupTypeClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupTypeReportHeading.
#    def enterReportGroupTypeReportHeading(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupTypeReportHeading.
#    def exitReportGroupTypeReportHeading(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupTypePageHeading.
#    def enterReportGroupTypePageHeading(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupTypePageHeading.
#    def exitReportGroupTypePageHeading(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupTypeControlHeading.
#    def enterReportGroupTypeControlHeading(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupTypeControlHeading.
#    def exitReportGroupTypeControlHeading(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupTypeDetail.
#    def enterReportGroupTypeDetail(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupTypeDetail.
#    def exitReportGroupTypeDetail(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupTypeControlFooting.
#    def enterReportGroupTypeControlFooting(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupTypeControlFooting.
#    def exitReportGroupTypeControlFooting(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupUsageClause.
#    def enterReportGroupUsageClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupUsageClause.
#    def exitReportGroupUsageClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupTypePageFooting.
#    def enterReportGroupTypePageFooting(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupTypePageFooting.
#    def exitReportGroupTypePageFooting(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupTypeReportFooting.
#    def enterReportGroupTypeReportFooting(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupTypeReportFooting.
#    def exitReportGroupTypeReportFooting(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportGroupValueClause.
#    def enterReportGroupValueClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportGroupValueClause.
#    def exitReportGroupValueClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#programLibrarySection.
#    def enterProgramLibrarySection(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#programLibrarySection.
#    def exitProgramLibrarySection(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#libraryDescriptionEntry.
#    def enterLibraryDescriptionEntry(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#libraryDescriptionEntry.
#    def exitLibraryDescriptionEntry(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#libraryDescriptionEntryFormat1.
#    def enterLibraryDescriptionEntryFormat1(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#libraryDescriptionEntryFormat1.
#    def exitLibraryDescriptionEntryFormat1(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#libraryDescriptionEntryFormat2.
#    def enterLibraryDescriptionEntryFormat2(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#libraryDescriptionEntryFormat2.
#    def exitLibraryDescriptionEntryFormat2(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#libraryAttributeClauseFormat1.
#    def enterLibraryAttributeClauseFormat1(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#libraryAttributeClauseFormat1.
#    def exitLibraryAttributeClauseFormat1(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#libraryAttributeClauseFormat2.
#    def enterLibraryAttributeClauseFormat2(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#libraryAttributeClauseFormat2.
#    def exitLibraryAttributeClauseFormat2(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#libraryAttributeFunction.
#    def enterLibraryAttributeFunction(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#libraryAttributeFunction.
#    def exitLibraryAttributeFunction(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#libraryAttributeParameter.
#    def enterLibraryAttributeParameter(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#libraryAttributeParameter.
#    def exitLibraryAttributeParameter(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#libraryAttributeTitle.
#    def enterLibraryAttributeTitle(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#libraryAttributeTitle.
#    def exitLibraryAttributeTitle(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#libraryEntryProcedureClauseFormat1.
#    def enterLibraryEntryProcedureClauseFormat1(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#libraryEntryProcedureClauseFormat1.
#    def exitLibraryEntryProcedureClauseFormat1(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#libraryEntryProcedureClauseFormat2.
#    def enterLibraryEntryProcedureClauseFormat2(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#libraryEntryProcedureClauseFormat2.
#    def exitLibraryEntryProcedureClauseFormat2(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#libraryEntryProcedureForClause.
#    def enterLibraryEntryProcedureForClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#libraryEntryProcedureForClause.
#    def exitLibraryEntryProcedureForClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#libraryEntryProcedureGivingClause.
#    def enterLibraryEntryProcedureGivingClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#libraryEntryProcedureGivingClause.
#    def exitLibraryEntryProcedureGivingClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#libraryEntryProcedureUsingClause.
#    def enterLibraryEntryProcedureUsingClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#libraryEntryProcedureUsingClause.
#    def exitLibraryEntryProcedureUsingClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#libraryEntryProcedureUsingName.
#    def enterLibraryEntryProcedureUsingName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#libraryEntryProcedureUsingName.
#    def exitLibraryEntryProcedureUsingName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#libraryEntryProcedureWithClause.
#    def enterLibraryEntryProcedureWithClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#libraryEntryProcedureWithClause.
#    def exitLibraryEntryProcedureWithClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#libraryEntryProcedureWithName.
#    def enterLibraryEntryProcedureWithName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#libraryEntryProcedureWithName.
#    def exitLibraryEntryProcedureWithName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#libraryIsCommonClause.
#    def enterLibraryIsCommonClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#libraryIsCommonClause.
#    def exitLibraryIsCommonClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#libraryIsGlobalClause.
#    def enterLibraryIsGlobalClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#libraryIsGlobalClause.
#    def exitLibraryIsGlobalClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataDescriptionEntry.
#    def enterDataDescriptionEntry(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataDescriptionEntry.
#    def exitDataDescriptionEntry(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataDescriptionEntryFormat1.
#    def enterDataDescriptionEntryFormat1(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataDescriptionEntryFormat1.
#    def exitDataDescriptionEntryFormat1(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataDescriptionEntryFormat2.
#    def enterDataDescriptionEntryFormat2(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataDescriptionEntryFormat2.
#    def exitDataDescriptionEntryFormat2(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataDescriptionEntryFormat3.
#    def enterDataDescriptionEntryFormat3(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataDescriptionEntryFormat3.
#    def exitDataDescriptionEntryFormat3(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataDescriptionEntryExecSql.
#    def enterDataDescriptionEntryExecSql(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataDescriptionEntryExecSql.
#    def exitDataDescriptionEntryExecSql(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataAlignedClause.
#    def enterDataAlignedClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataAlignedClause.
#    def exitDataAlignedClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataBlankWhenZeroClause.
#    def enterDataBlankWhenZeroClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataBlankWhenZeroClause.
#    def exitDataBlankWhenZeroClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataCommonOwnLocalClause.
#    def enterDataCommonOwnLocalClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataCommonOwnLocalClause.
#    def exitDataCommonOwnLocalClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataExternalClause.
#    def enterDataExternalClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataExternalClause.
#    def exitDataExternalClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataGlobalClause.
#    def enterDataGlobalClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataGlobalClause.
#    def exitDataGlobalClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataIntegerStringClause.
#    def enterDataIntegerStringClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataIntegerStringClause.
#    def exitDataIntegerStringClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataJustifiedClause.
#    def enterDataJustifiedClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataJustifiedClause.
#    def exitDataJustifiedClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataOccursClause.
#    def enterDataOccursClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataOccursClause.
#    def exitDataOccursClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataOccursTo.
#    def enterDataOccursTo(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataOccursTo.
#    def exitDataOccursTo(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataOccursSort.
#    def enterDataOccursSort(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataOccursSort.
#    def exitDataOccursSort(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataPictureClause.
#    def enterDataPictureClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataPictureClause.
#    def exitDataPictureClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#pictureString.
#    def enterPictureString(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#pictureString.
#    def exitPictureString(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#pictureChars.
#    def enterPictureChars(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#pictureChars.
#    def exitPictureChars(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#pictureCardinality.
#    def enterPictureCardinality(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#pictureCardinality.
#    def exitPictureCardinality(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataReceivedByClause.
#    def enterDataReceivedByClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataReceivedByClause.
#    def exitDataReceivedByClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataRecordAreaClause.
#    def enterDataRecordAreaClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataRecordAreaClause.
#    def exitDataRecordAreaClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataRedefinesClause.
#    def enterDataRedefinesClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataRedefinesClause.
#    def exitDataRedefinesClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataRenamesClause.
#    def enterDataRenamesClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataRenamesClause.
#    def exitDataRenamesClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataSignClause.
#    def enterDataSignClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataSignClause.
#    def exitDataSignClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataSynchronizedClause.
#    def enterDataSynchronizedClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataSynchronizedClause.
#    def exitDataSynchronizedClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataThreadLocalClause.
#    def enterDataThreadLocalClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataThreadLocalClause.
#    def exitDataThreadLocalClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataTypeClause.
#    def enterDataTypeClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataTypeClause.
#    def exitDataTypeClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataTypeDefClause.
#    def enterDataTypeDefClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataTypeDefClause.
#    def exitDataTypeDefClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataUsageClause.
#    def enterDataUsageClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataUsageClause.
#    def exitDataUsageClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataUsingClause.
#    def enterDataUsingClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataUsingClause.
#    def exitDataUsingClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataValueClause.
#    def enterDataValueClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataValueClause.
#    def exitDataValueClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataValueInterval.
#    def enterDataValueInterval(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataValueInterval.
#    def exitDataValueInterval(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataValueIntervalFrom.
#    def enterDataValueIntervalFrom(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataValueIntervalFrom.
#    def exitDataValueIntervalFrom(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataValueIntervalTo.
#    def enterDataValueIntervalTo(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataValueIntervalTo.
#    def exitDataValueIntervalTo(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataWithLowerBoundsClause.
#    def enterDataWithLowerBoundsClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataWithLowerBoundsClause.
#    def exitDataWithLowerBoundsClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#procedureDivision.
#    def enterProcedureDivision(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#procedureDivision.
#    def exitProcedureDivision(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#procedureDivisionUsingClause.
#    def enterProcedureDivisionUsingClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#procedureDivisionUsingClause.
#    def exitProcedureDivisionUsingClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#procedureDivisionGivingClause.
#    def enterProcedureDivisionGivingClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#procedureDivisionGivingClause.
#    def exitProcedureDivisionGivingClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#procedureDivisionUsingParameter.
#    def enterProcedureDivisionUsingParameter(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#procedureDivisionUsingParameter.
#    def exitProcedureDivisionUsingParameter(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#procedureDivisionByReferencePhrase.
#    def enterProcedureDivisionByReferencePhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#procedureDivisionByReferencePhrase.
#    def exitProcedureDivisionByReferencePhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#procedureDivisionByReference.
#    def enterProcedureDivisionByReference(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#procedureDivisionByReference.
#    def exitProcedureDivisionByReference(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#procedureDivisionByValuePhrase.
#    def enterProcedureDivisionByValuePhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#procedureDivisionByValuePhrase.
#    def exitProcedureDivisionByValuePhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#procedureDivisionByValue.
#    def enterProcedureDivisionByValue(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#procedureDivisionByValue.
#    def exitProcedureDivisionByValue(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#procedureDeclaratives.
#    def enterProcedureDeclaratives(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#procedureDeclaratives.
#    def exitProcedureDeclaratives(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#procedureDeclarative.
#    def enterProcedureDeclarative(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#procedureDeclarative.
#    def exitProcedureDeclarative(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#procedureSectionHeader.
#    def enterProcedureSectionHeader(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#procedureSectionHeader.
#    def exitProcedureSectionHeader(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#procedureDivisionBody.
#    def enterProcedureDivisionBody(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#procedureDivisionBody.
#    def exitProcedureDivisionBody(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#procedureSection.
#    def enterProcedureSection(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#procedureSection.
#    def exitProcedureSection(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#paragraphs.
#    def enterParagraphs(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#paragraphs.
#    def exitParagraphs(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#paragraph.
#    def enterParagraph(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#paragraph.
#    def exitParagraph(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sentence.
#    def enterSentence(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sentence.
#    def exitSentence(self, ctx):
#        pass
#
#    # Enter a parse tree produced by Cobol85Parser#statement.
#    def enterStatement(self, ctx):
#        pass
#        return self.add_node('enterStatement', ctx)
#
#    # Exit a parse tree produced by Cobol85Parser#statement.
#    def exitStatement(self, ctx):
#        pass
#        return self.pop_stack('exitStatement', ctx)
#
#
#    # Enter a parse tree produced by Cobol85Parser#acceptStatement.
#    def enterAcceptStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#acceptStatement.
#    def exitAcceptStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#acceptFromDateStatement.
#    def enterAcceptFromDateStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#acceptFromDateStatement.
#    def exitAcceptFromDateStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#acceptFromMnemonicStatement.
#    def enterAcceptFromMnemonicStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#acceptFromMnemonicStatement.
#    def exitAcceptFromMnemonicStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#acceptFromEscapeKeyStatement.
#    def enterAcceptFromEscapeKeyStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#acceptFromEscapeKeyStatement.
#    def exitAcceptFromEscapeKeyStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#acceptMessageCountStatement.
#    def enterAcceptMessageCountStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#acceptMessageCountStatement.
#    def exitAcceptMessageCountStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#addStatement.
#    def enterAddStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#addStatement.
#    def exitAddStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#addToStatement.
#    def enterAddToStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#addToStatement.
#    def exitAddToStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#addToGivingStatement.
#    def enterAddToGivingStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#addToGivingStatement.
#    def exitAddToGivingStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#addCorrespondingStatement.
#    def enterAddCorrespondingStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#addCorrespondingStatement.
#    def exitAddCorrespondingStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#addFrom.
#    def enterAddFrom(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#addFrom.
#    def exitAddFrom(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#addTo.
#    def enterAddTo(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#addTo.
#    def exitAddTo(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#addToGiving.
#    def enterAddToGiving(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#addToGiving.
#    def exitAddToGiving(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#addGiving.
#    def enterAddGiving(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#addGiving.
#    def exitAddGiving(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#alteredGoTo.
#    def enterAlteredGoTo(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#alteredGoTo.
#    def exitAlteredGoTo(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#alterStatement.
#    def enterAlterStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#alterStatement.
#    def exitAlterStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#alterProceedTo.
#    def enterAlterProceedTo(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#alterProceedTo.
#    def exitAlterProceedTo(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#callStatement.
#    def enterCallStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#callStatement.
#    def exitCallStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#callUsingPhrase.
#    def enterCallUsingPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#callUsingPhrase.
#    def exitCallUsingPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#callUsingParameter.
#    def enterCallUsingParameter(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#callUsingParameter.
#    def exitCallUsingParameter(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#callByReferencePhrase.
#    def enterCallByReferencePhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#callByReferencePhrase.
#    def exitCallByReferencePhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#callByReference.
#    def enterCallByReference(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#callByReference.
#    def exitCallByReference(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#callByValuePhrase.
#    def enterCallByValuePhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#callByValuePhrase.
#    def exitCallByValuePhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#callByValue.
#    def enterCallByValue(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#callByValue.
#    def exitCallByValue(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#callByContentPhrase.
#    def enterCallByContentPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#callByContentPhrase.
#    def exitCallByContentPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#callByContent.
#    def enterCallByContent(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#callByContent.
#    def exitCallByContent(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#callGivingPhrase.
#    def enterCallGivingPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#callGivingPhrase.
#    def exitCallGivingPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#cancelStatement.
#    def enterCancelStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#cancelStatement.
#    def exitCancelStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#cancelCall.
#    def enterCancelCall(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#cancelCall.
#    def exitCancelCall(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#closeStatement.
#    def enterCloseStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#closeStatement.
#    def exitCloseStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#closeFile.
#    def enterCloseFile(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#closeFile.
#    def exitCloseFile(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#closeReelUnitStatement.
#    def enterCloseReelUnitStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#closeReelUnitStatement.
#    def exitCloseReelUnitStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#closeRelativeStatement.
#    def enterCloseRelativeStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#closeRelativeStatement.
#    def exitCloseRelativeStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#closePortFileIOStatement.
#    def enterClosePortFileIOStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#closePortFileIOStatement.
#    def exitClosePortFileIOStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#closePortFileIOUsing.
#    def enterClosePortFileIOUsing(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#closePortFileIOUsing.
#    def exitClosePortFileIOUsing(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#closePortFileIOUsingCloseDisposition.
#    def enterClosePortFileIOUsingCloseDisposition(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#closePortFileIOUsingCloseDisposition.
#    def exitClosePortFileIOUsingCloseDisposition(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#closePortFileIOUsingAssociatedData.
#    def enterClosePortFileIOUsingAssociatedData(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#closePortFileIOUsingAssociatedData.
#    def exitClosePortFileIOUsingAssociatedData(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#closePortFileIOUsingAssociatedDataLength.
#    def enterClosePortFileIOUsingAssociatedDataLength(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#closePortFileIOUsingAssociatedDataLength.
#    def exitClosePortFileIOUsingAssociatedDataLength(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#computeStatement.
#    def enterComputeStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#computeStatement.
#    def exitComputeStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#computeStore.
#    def enterComputeStore(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#computeStore.
#    def exitComputeStore(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#continueStatement.
#    def enterContinueStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#continueStatement.
#    def exitContinueStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#deleteStatement.
#    def enterDeleteStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#deleteStatement.
#    def exitDeleteStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#disableStatement.
#    def enterDisableStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#disableStatement.
#    def exitDisableStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#displayStatement.
#    def enterDisplayStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#displayStatement.
#    def exitDisplayStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#displayOperand.
#    def enterDisplayOperand(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#displayOperand.
#    def exitDisplayOperand(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#displayAt.
#    def enterDisplayAt(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#displayAt.
#    def exitDisplayAt(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#displayUpon.
#    def enterDisplayUpon(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#displayUpon.
#    def exitDisplayUpon(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#displayWith.
#    def enterDisplayWith(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#displayWith.
#    def exitDisplayWith(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#divideStatement.
#    def enterDivideStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#divideStatement.
#    def exitDivideStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#divideIntoStatement.
#    def enterDivideIntoStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#divideIntoStatement.
#    def exitDivideIntoStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#divideIntoGivingStatement.
#    def enterDivideIntoGivingStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#divideIntoGivingStatement.
#    def exitDivideIntoGivingStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#divideByGivingStatement.
#    def enterDivideByGivingStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#divideByGivingStatement.
#    def exitDivideByGivingStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#divideGivingPhrase.
#    def enterDivideGivingPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#divideGivingPhrase.
#    def exitDivideGivingPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#divideInto.
#    def enterDivideInto(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#divideInto.
#    def exitDivideInto(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#divideGiving.
#    def enterDivideGiving(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#divideGiving.
#    def exitDivideGiving(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#divideRemainder.
#    def enterDivideRemainder(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#divideRemainder.
#    def exitDivideRemainder(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#enableStatement.
#    def enterEnableStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#enableStatement.
#    def exitEnableStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#entryStatement.
#    def enterEntryStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#entryStatement.
#    def exitEntryStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#evaluateStatement.
#    def enterEvaluateStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#evaluateStatement.
#    def exitEvaluateStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#evaluateSelect.
#    def enterEvaluateSelect(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#evaluateSelect.
#    def exitEvaluateSelect(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#evaluateAlsoSelect.
#    def enterEvaluateAlsoSelect(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#evaluateAlsoSelect.
#    def exitEvaluateAlsoSelect(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#evaluateWhenPhrase.
#    def enterEvaluateWhenPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#evaluateWhenPhrase.
#    def exitEvaluateWhenPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#evaluateWhen.
#    def enterEvaluateWhen(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#evaluateWhen.
#    def exitEvaluateWhen(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#evaluateCondition.
#    def enterEvaluateCondition(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#evaluateCondition.
#    def exitEvaluateCondition(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#evaluateThrough.
#    def enterEvaluateThrough(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#evaluateThrough.
#    def exitEvaluateThrough(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#evaluateAlsoCondition.
#    def enterEvaluateAlsoCondition(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#evaluateAlsoCondition.
#    def exitEvaluateAlsoCondition(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#evaluateWhenOther.
#    def enterEvaluateWhenOther(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#evaluateWhenOther.
#    def exitEvaluateWhenOther(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#evaluateValue.
#    def enterEvaluateValue(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#evaluateValue.
#    def exitEvaluateValue(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#execCicsStatement.
#    def enterExecCicsStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#execCicsStatement.
#    def exitExecCicsStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#execSqlStatement.
#    def enterExecSqlStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#execSqlStatement.
#    def exitExecSqlStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#execSqlImsStatement.
#    def enterExecSqlImsStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#execSqlImsStatement.
#    def exitExecSqlImsStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#exhibitStatement.
#    def enterExhibitStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#exhibitStatement.
#    def exitExhibitStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#exhibitOperand.
#    def enterExhibitOperand(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#exhibitOperand.
#    def exitExhibitOperand(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#exitStatement.
#    def enterExitStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#exitStatement.
#    def exitExitStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#generateStatement.
#    def enterGenerateStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#generateStatement.
#    def exitGenerateStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#gobackStatement.
#    def enterGobackStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#gobackStatement.
#    def exitGobackStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#goToStatement.
#    def enterGoToStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#goToStatement.
#    def exitGoToStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#goToStatementSimple.
#    def enterGoToStatementSimple(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#goToStatementSimple.
#    def exitGoToStatementSimple(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#goToDependingOnStatement.
#    def enterGoToDependingOnStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#goToDependingOnStatement.
#    def exitGoToDependingOnStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#ifStatement.
#    def enterIfStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#ifStatement.
#    def exitIfStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#ifThen.
#    def enterIfThen(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#ifThen.
#    def exitIfThen(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#ifElse.
#    def enterIfElse(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#ifElse.
#    def exitIfElse(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#initializeStatement.
#    def enterInitializeStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#initializeStatement.
#    def exitInitializeStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#initializeReplacingPhrase.
#    def enterInitializeReplacingPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#initializeReplacingPhrase.
#    def exitInitializeReplacingPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#initializeReplacingBy.
#    def enterInitializeReplacingBy(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#initializeReplacingBy.
#    def exitInitializeReplacingBy(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#initiateStatement.
#    def enterInitiateStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#initiateStatement.
#    def exitInitiateStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#inspectStatement.
#    def enterInspectStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#inspectStatement.
#    def exitInspectStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#inspectTallyingPhrase.
#    def enterInspectTallyingPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#inspectTallyingPhrase.
#    def exitInspectTallyingPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#inspectReplacingPhrase.
#    def enterInspectReplacingPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#inspectReplacingPhrase.
#    def exitInspectReplacingPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#inspectTallyingReplacingPhrase.
#    def enterInspectTallyingReplacingPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#inspectTallyingReplacingPhrase.
#    def exitInspectTallyingReplacingPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#inspectConvertingPhrase.
#    def enterInspectConvertingPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#inspectConvertingPhrase.
#    def exitInspectConvertingPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#inspectFor.
#    def enterInspectFor(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#inspectFor.
#    def exitInspectFor(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#inspectCharacters.
#    def enterInspectCharacters(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#inspectCharacters.
#    def exitInspectCharacters(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#inspectReplacingCharacters.
#    def enterInspectReplacingCharacters(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#inspectReplacingCharacters.
#    def exitInspectReplacingCharacters(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#inspectAllLeadings.
#    def enterInspectAllLeadings(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#inspectAllLeadings.
#    def exitInspectAllLeadings(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#inspectReplacingAllLeadings.
#    def enterInspectReplacingAllLeadings(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#inspectReplacingAllLeadings.
#    def exitInspectReplacingAllLeadings(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#inspectAllLeading.
#    def enterInspectAllLeading(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#inspectAllLeading.
#    def exitInspectAllLeading(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#inspectReplacingAllLeading.
#    def enterInspectReplacingAllLeading(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#inspectReplacingAllLeading.
#    def exitInspectReplacingAllLeading(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#inspectBy.
#    def enterInspectBy(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#inspectBy.
#    def exitInspectBy(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#inspectTo.
#    def enterInspectTo(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#inspectTo.
#    def exitInspectTo(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#inspectBeforeAfter.
#    def enterInspectBeforeAfter(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#inspectBeforeAfter.
#    def exitInspectBeforeAfter(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#mergeStatement.
#    def enterMergeStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#mergeStatement.
#    def exitMergeStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#mergeOnKeyClause.
#    def enterMergeOnKeyClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#mergeOnKeyClause.
#    def exitMergeOnKeyClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#mergeCollatingSequencePhrase.
#    def enterMergeCollatingSequencePhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#mergeCollatingSequencePhrase.
#    def exitMergeCollatingSequencePhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#mergeCollatingAlphanumeric.
#    def enterMergeCollatingAlphanumeric(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#mergeCollatingAlphanumeric.
#    def exitMergeCollatingAlphanumeric(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#mergeCollatingNational.
#    def enterMergeCollatingNational(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#mergeCollatingNational.
#    def exitMergeCollatingNational(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#mergeUsing.
#    def enterMergeUsing(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#mergeUsing.
#    def exitMergeUsing(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#mergeOutputProcedurePhrase.
#    def enterMergeOutputProcedurePhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#mergeOutputProcedurePhrase.
#    def exitMergeOutputProcedurePhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#mergeOutputThrough.
#    def enterMergeOutputThrough(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#mergeOutputThrough.
#    def exitMergeOutputThrough(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#mergeGivingPhrase.
#    def enterMergeGivingPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#mergeGivingPhrase.
#    def exitMergeGivingPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#mergeGiving.
#    def enterMergeGiving(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#mergeGiving.
#    def exitMergeGiving(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#moveStatement.
#    def enterMoveStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#moveStatement.
#    def exitMoveStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#moveToStatement.
#    def enterMoveToStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#moveToStatement.
#    def exitMoveToStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#moveToSendingArea.
#    def enterMoveToSendingArea(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#moveToSendingArea.
#    def exitMoveToSendingArea(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#moveCorrespondingToStatement.
#    def enterMoveCorrespondingToStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#moveCorrespondingToStatement.
#    def exitMoveCorrespondingToStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#moveCorrespondingToSendingArea.
#    def enterMoveCorrespondingToSendingArea(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#moveCorrespondingToSendingArea.
#    def exitMoveCorrespondingToSendingArea(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#multiplyStatement.
#    def enterMultiplyStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#multiplyStatement.
#    def exitMultiplyStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#multiplyRegular.
#    def enterMultiplyRegular(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#multiplyRegular.
#    def exitMultiplyRegular(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#multiplyRegularOperand.
#    def enterMultiplyRegularOperand(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#multiplyRegularOperand.
#    def exitMultiplyRegularOperand(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#multiplyGiving.
#    def enterMultiplyGiving(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#multiplyGiving.
#    def exitMultiplyGiving(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#multiplyGivingOperand.
#    def enterMultiplyGivingOperand(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#multiplyGivingOperand.
#    def exitMultiplyGivingOperand(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#multiplyGivingResult.
#    def enterMultiplyGivingResult(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#multiplyGivingResult.
#    def exitMultiplyGivingResult(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#openStatement.
#    def enterOpenStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#openStatement.
#    def exitOpenStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#openInputStatement.
#    def enterOpenInputStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#openInputStatement.
#    def exitOpenInputStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#openInput.
#    def enterOpenInput(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#openInput.
#    def exitOpenInput(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#openOutputStatement.
#    def enterOpenOutputStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#openOutputStatement.
#    def exitOpenOutputStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#openOutput.
#    def enterOpenOutput(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#openOutput.
#    def exitOpenOutput(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#openIOStatement.
#    def enterOpenIOStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#openIOStatement.
#    def exitOpenIOStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#openExtendStatement.
#    def enterOpenExtendStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#openExtendStatement.
#    def exitOpenExtendStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#performStatement.
#    def enterPerformStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#performStatement.
#    def exitPerformStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#performInlineStatement.
#    def enterPerformInlineStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#performInlineStatement.
#    def exitPerformInlineStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#performProcedureStatement.
#    def enterPerformProcedureStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#performProcedureStatement.
#    def exitPerformProcedureStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#performType.
#    def enterPerformType(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#performType.
#    def exitPerformType(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#performTimes.
#    def enterPerformTimes(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#performTimes.
#    def exitPerformTimes(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#performUntil.
#    def enterPerformUntil(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#performUntil.
#    def exitPerformUntil(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#performVarying.
#    def enterPerformVarying(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#performVarying.
#    def exitPerformVarying(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#performVaryingClause.
#    def enterPerformVaryingClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#performVaryingClause.
#    def exitPerformVaryingClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#performVaryingPhrase.
#    def enterPerformVaryingPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#performVaryingPhrase.
#    def exitPerformVaryingPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#performAfter.
#    def enterPerformAfter(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#performAfter.
#    def exitPerformAfter(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#performFrom.
#    def enterPerformFrom(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#performFrom.
#    def exitPerformFrom(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#performBy.
#    def enterPerformBy(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#performBy.
#    def exitPerformBy(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#performTestClause.
#    def enterPerformTestClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#performTestClause.
#    def exitPerformTestClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#purgeStatement.
#    def enterPurgeStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#purgeStatement.
#    def exitPurgeStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#readStatement.
#    def enterReadStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#readStatement.
#    def exitReadStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#readInto.
#    def enterReadInto(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#readInto.
#    def exitReadInto(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#readWith.
#    def enterReadWith(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#readWith.
#    def exitReadWith(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#readKey.
#    def enterReadKey(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#readKey.
#    def exitReadKey(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#receiveStatement.
#    def enterReceiveStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#receiveStatement.
#    def exitReceiveStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#receiveFromStatement.
#    def enterReceiveFromStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#receiveFromStatement.
#    def exitReceiveFromStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#receiveFrom.
#    def enterReceiveFrom(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#receiveFrom.
#    def exitReceiveFrom(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#receiveIntoStatement.
#    def enterReceiveIntoStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#receiveIntoStatement.
#    def exitReceiveIntoStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#receiveNoData.
#    def enterReceiveNoData(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#receiveNoData.
#    def exitReceiveNoData(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#receiveWithData.
#    def enterReceiveWithData(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#receiveWithData.
#    def exitReceiveWithData(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#receiveBefore.
#    def enterReceiveBefore(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#receiveBefore.
#    def exitReceiveBefore(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#receiveWith.
#    def enterReceiveWith(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#receiveWith.
#    def exitReceiveWith(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#receiveThread.
#    def enterReceiveThread(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#receiveThread.
#    def exitReceiveThread(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#receiveSize.
#    def enterReceiveSize(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#receiveSize.
#    def exitReceiveSize(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#receiveStatus.
#    def enterReceiveStatus(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#receiveStatus.
#    def exitReceiveStatus(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#releaseStatement.
#    def enterReleaseStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#releaseStatement.
#    def exitReleaseStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#returnStatement.
#    def enterReturnStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#returnStatement.
#    def exitReturnStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#returnInto.
#    def enterReturnInto(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#returnInto.
#    def exitReturnInto(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#rewriteStatement.
#    def enterRewriteStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#rewriteStatement.
#    def exitRewriteStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#rewriteFrom.
#    def enterRewriteFrom(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#rewriteFrom.
#    def exitRewriteFrom(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#searchStatement.
#    def enterSearchStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#searchStatement.
#    def exitSearchStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#searchVarying.
#    def enterSearchVarying(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#searchVarying.
#    def exitSearchVarying(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#searchWhen.
#    def enterSearchWhen(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#searchWhen.
#    def exitSearchWhen(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sendStatement.
#    def enterSendStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sendStatement.
#    def exitSendStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sendStatementSync.
#    def enterSendStatementSync(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sendStatementSync.
#    def exitSendStatementSync(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sendStatementAsync.
#    def enterSendStatementAsync(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sendStatementAsync.
#    def exitSendStatementAsync(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sendFromPhrase.
#    def enterSendFromPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sendFromPhrase.
#    def exitSendFromPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sendWithPhrase.
#    def enterSendWithPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sendWithPhrase.
#    def exitSendWithPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sendReplacingPhrase.
#    def enterSendReplacingPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sendReplacingPhrase.
#    def exitSendReplacingPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sendAdvancingPhrase.
#    def enterSendAdvancingPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sendAdvancingPhrase.
#    def exitSendAdvancingPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sendAdvancingPage.
#    def enterSendAdvancingPage(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sendAdvancingPage.
#    def exitSendAdvancingPage(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sendAdvancingLines.
#    def enterSendAdvancingLines(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sendAdvancingLines.
#    def exitSendAdvancingLines(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sendAdvancingMnemonic.
#    def enterSendAdvancingMnemonic(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sendAdvancingMnemonic.
#    def exitSendAdvancingMnemonic(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#setStatement.
#    def enterSetStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#setStatement.
#    def exitSetStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#setToStatement.
#    def enterSetToStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#setToStatement.
#    def exitSetToStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#setUpDownByStatement.
#    def enterSetUpDownByStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#setUpDownByStatement.
#    def exitSetUpDownByStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#setTo.
#    def enterSetTo(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#setTo.
#    def exitSetTo(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#setToValue.
#    def enterSetToValue(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#setToValue.
#    def exitSetToValue(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#setByValue.
#    def enterSetByValue(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#setByValue.
#    def exitSetByValue(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sortStatement.
#    def enterSortStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sortStatement.
#    def exitSortStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sortOnKeyClause.
#    def enterSortOnKeyClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sortOnKeyClause.
#    def exitSortOnKeyClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sortDuplicatesPhrase.
#    def enterSortDuplicatesPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sortDuplicatesPhrase.
#    def exitSortDuplicatesPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sortCollatingSequencePhrase.
#    def enterSortCollatingSequencePhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sortCollatingSequencePhrase.
#    def exitSortCollatingSequencePhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sortCollatingAlphanumeric.
#    def enterSortCollatingAlphanumeric(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sortCollatingAlphanumeric.
#    def exitSortCollatingAlphanumeric(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sortCollatingNational.
#    def enterSortCollatingNational(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sortCollatingNational.
#    def exitSortCollatingNational(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sortInputProcedurePhrase.
#    def enterSortInputProcedurePhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sortInputProcedurePhrase.
#    def exitSortInputProcedurePhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sortInputThrough.
#    def enterSortInputThrough(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sortInputThrough.
#    def exitSortInputThrough(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sortUsing.
#    def enterSortUsing(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sortUsing.
#    def exitSortUsing(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sortOutputProcedurePhrase.
#    def enterSortOutputProcedurePhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sortOutputProcedurePhrase.
#    def exitSortOutputProcedurePhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sortOutputThrough.
#    def enterSortOutputThrough(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sortOutputThrough.
#    def exitSortOutputThrough(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sortGivingPhrase.
#    def enterSortGivingPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sortGivingPhrase.
#    def exitSortGivingPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sortGiving.
#    def enterSortGiving(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sortGiving.
#    def exitSortGiving(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#startStatement.
#    def enterStartStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#startStatement.
#    def exitStartStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#startKey.
#    def enterStartKey(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#startKey.
#    def exitStartKey(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#stopStatement.
#    def enterStopStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#stopStatement.
#    def exitStopStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#stopStatementGiving.
#    def enterStopStatementGiving(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#stopStatementGiving.
#    def exitStopStatementGiving(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#stringStatement.
#    def enterStringStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#stringStatement.
#    def exitStringStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#stringSendingPhrase.
#    def enterStringSendingPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#stringSendingPhrase.
#    def exitStringSendingPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#stringSending.
#    def enterStringSending(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#stringSending.
#    def exitStringSending(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#stringDelimitedByPhrase.
#    def enterStringDelimitedByPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#stringDelimitedByPhrase.
#    def exitStringDelimitedByPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#stringForPhrase.
#    def enterStringForPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#stringForPhrase.
#    def exitStringForPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#stringIntoPhrase.
#    def enterStringIntoPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#stringIntoPhrase.
#    def exitStringIntoPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#stringWithPointerPhrase.
#    def enterStringWithPointerPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#stringWithPointerPhrase.
#    def exitStringWithPointerPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#subtractStatement.
#    def enterSubtractStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#subtractStatement.
#    def exitSubtractStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#subtractFromStatement.
#    def enterSubtractFromStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#subtractFromStatement.
#    def exitSubtractFromStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#subtractFromGivingStatement.
#    def enterSubtractFromGivingStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#subtractFromGivingStatement.
#    def exitSubtractFromGivingStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#subtractCorrespondingStatement.
#    def enterSubtractCorrespondingStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#subtractCorrespondingStatement.
#    def exitSubtractCorrespondingStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#subtractSubtrahend.
#    def enterSubtractSubtrahend(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#subtractSubtrahend.
#    def exitSubtractSubtrahend(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#subtractMinuend.
#    def enterSubtractMinuend(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#subtractMinuend.
#    def exitSubtractMinuend(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#subtractMinuendGiving.
#    def enterSubtractMinuendGiving(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#subtractMinuendGiving.
#    def exitSubtractMinuendGiving(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#subtractGiving.
#    def enterSubtractGiving(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#subtractGiving.
#    def exitSubtractGiving(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#subtractMinuendCorresponding.
#    def enterSubtractMinuendCorresponding(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#subtractMinuendCorresponding.
#    def exitSubtractMinuendCorresponding(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#terminateStatement.
#    def enterTerminateStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#terminateStatement.
#    def exitTerminateStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#unstringStatement.
#    def enterUnstringStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#unstringStatement.
#    def exitUnstringStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#unstringSendingPhrase.
#    def enterUnstringSendingPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#unstringSendingPhrase.
#    def exitUnstringSendingPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#unstringDelimitedByPhrase.
#    def enterUnstringDelimitedByPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#unstringDelimitedByPhrase.
#    def exitUnstringDelimitedByPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#unstringOrAllPhrase.
#    def enterUnstringOrAllPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#unstringOrAllPhrase.
#    def exitUnstringOrAllPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#unstringIntoPhrase.
#    def enterUnstringIntoPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#unstringIntoPhrase.
#    def exitUnstringIntoPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#unstringInto.
#    def enterUnstringInto(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#unstringInto.
#    def exitUnstringInto(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#unstringDelimiterIn.
#    def enterUnstringDelimiterIn(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#unstringDelimiterIn.
#    def exitUnstringDelimiterIn(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#unstringCountIn.
#    def enterUnstringCountIn(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#unstringCountIn.
#    def exitUnstringCountIn(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#unstringWithPointerPhrase.
#    def enterUnstringWithPointerPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#unstringWithPointerPhrase.
#    def exitUnstringWithPointerPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#unstringTallyingPhrase.
#    def enterUnstringTallyingPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#unstringTallyingPhrase.
#    def exitUnstringTallyingPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#useStatement.
#    def enterUseStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#useStatement.
#    def exitUseStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#useAfterClause.
#    def enterUseAfterClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#useAfterClause.
#    def exitUseAfterClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#useAfterOn.
#    def enterUseAfterOn(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#useAfterOn.
#    def exitUseAfterOn(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#useDebugClause.
#    def enterUseDebugClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#useDebugClause.
#    def exitUseDebugClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#useDebugOn.
#    def enterUseDebugOn(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#useDebugOn.
#    def exitUseDebugOn(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#writeStatement.
#    def enterWriteStatement(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#writeStatement.
#    def exitWriteStatement(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#writeFromPhrase.
#    def enterWriteFromPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#writeFromPhrase.
#    def exitWriteFromPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#writeAdvancingPhrase.
#    def enterWriteAdvancingPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#writeAdvancingPhrase.
#    def exitWriteAdvancingPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#writeAdvancingPage.
#    def enterWriteAdvancingPage(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#writeAdvancingPage.
#    def exitWriteAdvancingPage(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#writeAdvancingLines.
#    def enterWriteAdvancingLines(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#writeAdvancingLines.
#    def exitWriteAdvancingLines(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#writeAdvancingMnemonic.
#    def enterWriteAdvancingMnemonic(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#writeAdvancingMnemonic.
#    def exitWriteAdvancingMnemonic(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#writeAtEndOfPagePhrase.
#    def enterWriteAtEndOfPagePhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#writeAtEndOfPagePhrase.
#    def exitWriteAtEndOfPagePhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#writeNotAtEndOfPagePhrase.
#    def enterWriteNotAtEndOfPagePhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#writeNotAtEndOfPagePhrase.
#    def exitWriteNotAtEndOfPagePhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#atEndPhrase.
#    def enterAtEndPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#atEndPhrase.
#    def exitAtEndPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#notAtEndPhrase.
#    def enterNotAtEndPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#notAtEndPhrase.
#    def exitNotAtEndPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#invalidKeyPhrase.
#    def enterInvalidKeyPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#invalidKeyPhrase.
#    def exitInvalidKeyPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#notInvalidKeyPhrase.
#    def enterNotInvalidKeyPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#notInvalidKeyPhrase.
#    def exitNotInvalidKeyPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#onOverflowPhrase.
#    def enterOnOverflowPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#onOverflowPhrase.
#    def exitOnOverflowPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#notOnOverflowPhrase.
#    def enterNotOnOverflowPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#notOnOverflowPhrase.
#    def exitNotOnOverflowPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#onSizeErrorPhrase.
#    def enterOnSizeErrorPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#onSizeErrorPhrase.
#    def exitOnSizeErrorPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#notOnSizeErrorPhrase.
#    def enterNotOnSizeErrorPhrase(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#notOnSizeErrorPhrase.
#    def exitNotOnSizeErrorPhrase(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#onExceptionClause.
#    def enterOnExceptionClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#onExceptionClause.
#    def exitOnExceptionClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#notOnExceptionClause.
#    def enterNotOnExceptionClause(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#notOnExceptionClause.
#    def exitNotOnExceptionClause(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#arithmeticExpression.
#    def enterArithmeticExpression(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#arithmeticExpression.
#    def exitArithmeticExpression(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#plusMinus.
#    def enterPlusMinus(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#plusMinus.
#    def exitPlusMinus(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#multDivs.
#    def enterMultDivs(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#multDivs.
#    def exitMultDivs(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#multDiv.
#    def enterMultDiv(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#multDiv.
#    def exitMultDiv(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#powers.
#    def enterPowers(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#powers.
#    def exitPowers(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#power.
#    def enterPower(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#power.
#    def exitPower(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#basis.
#    def enterBasis(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#basis.
#    def exitBasis(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#condition.
#    def enterCondition(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#condition.
#    def exitCondition(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#andOrCondition.
#    def enterAndOrCondition(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#andOrCondition.
#    def exitAndOrCondition(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#combinableCondition.
#    def enterCombinableCondition(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#combinableCondition.
#    def exitCombinableCondition(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#simpleCondition.
#    def enterSimpleCondition(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#simpleCondition.
#    def exitSimpleCondition(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#classCondition.
#    def enterClassCondition(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#classCondition.
#    def exitClassCondition(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#conditionNameReference.
#    def enterConditionNameReference(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#conditionNameReference.
#    def exitConditionNameReference(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#conditionNameSubscriptReference.
#    def enterConditionNameSubscriptReference(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#conditionNameSubscriptReference.
#    def exitConditionNameSubscriptReference(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#relationCondition.
#    def enterRelationCondition(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#relationCondition.
#    def exitRelationCondition(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#relationSignCondition.
#    def enterRelationSignCondition(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#relationSignCondition.
#    def exitRelationSignCondition(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#relationArithmeticComparison.
#    def enterRelationArithmeticComparison(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#relationArithmeticComparison.
#    def exitRelationArithmeticComparison(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#relationCombinedComparison.
#    def enterRelationCombinedComparison(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#relationCombinedComparison.
#    def exitRelationCombinedComparison(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#relationCombinedCondition.
#    def enterRelationCombinedCondition(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#relationCombinedCondition.
#    def exitRelationCombinedCondition(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#relationalOperator.
#    def enterRelationalOperator(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#relationalOperator.
#    def exitRelationalOperator(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#abbreviation.
#    def enterAbbreviation(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#abbreviation.
#    def exitAbbreviation(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#identifier.
#    def enterIdentifier(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#identifier.
#    def exitIdentifier(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#tableCall.
#    def enterTableCall(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#tableCall.
#    def exitTableCall(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#functionCall.
#    def enterFunctionCall(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#functionCall.
#    def exitFunctionCall(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#referenceModifier.
#    def enterReferenceModifier(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#referenceModifier.
#    def exitReferenceModifier(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#characterPosition.
#    def enterCharacterPosition(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#characterPosition.
#    def exitCharacterPosition(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#length.
#    def enterLength(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#length.
#    def exitLength(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#subscript.
#    def enterSubscript(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#subscript.
#    def exitSubscript(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#argument.
#    def enterArgument(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#argument.
#    def exitArgument(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#qualifiedDataName.
#    def enterQualifiedDataName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#qualifiedDataName.
#    def exitQualifiedDataName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#qualifiedDataNameFormat1.
#    def enterQualifiedDataNameFormat1(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#qualifiedDataNameFormat1.
#    def exitQualifiedDataNameFormat1(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#qualifiedDataNameFormat2.
#    def enterQualifiedDataNameFormat2(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#qualifiedDataNameFormat2.
#    def exitQualifiedDataNameFormat2(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#qualifiedDataNameFormat3.
#    def enterQualifiedDataNameFormat3(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#qualifiedDataNameFormat3.
#    def exitQualifiedDataNameFormat3(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#qualifiedDataNameFormat4.
#    def enterQualifiedDataNameFormat4(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#qualifiedDataNameFormat4.
#    def exitQualifiedDataNameFormat4(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#qualifiedInData.
#    def enterQualifiedInData(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#qualifiedInData.
#    def exitQualifiedInData(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#inData.
#    def enterInData(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#inData.
#    def exitInData(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#inFile.
#    def enterInFile(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#inFile.
#    def exitInFile(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#inMnemonic.
#    def enterInMnemonic(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#inMnemonic.
#    def exitInMnemonic(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#inSection.
#    def enterInSection(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#inSection.
#    def exitInSection(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#inLibrary.
#    def enterInLibrary(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#inLibrary.
#    def exitInLibrary(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#inTable.
#    def enterInTable(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#inTable.
#    def exitInTable(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#alphabetName.
#    def enterAlphabetName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#alphabetName.
#    def exitAlphabetName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#assignmentName.
#    def enterAssignmentName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#assignmentName.
#    def exitAssignmentName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#basisName.
#    def enterBasisName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#basisName.
#    def exitBasisName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#cdName.
#    def enterCdName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#cdName.
#    def exitCdName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#className.
#    def enterClassName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#className.
#    def exitClassName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#computerName.
#    def enterComputerName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#computerName.
#    def exitComputerName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#conditionName.
#    def enterConditionName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#conditionName.
#    def exitConditionName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataName.
#    def enterDataName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataName.
#    def exitDataName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#dataDescName.
#    def enterDataDescName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#dataDescName.
#    def exitDataDescName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#environmentName.
#    def enterEnvironmentName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#environmentName.
#    def exitEnvironmentName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#fileName.
#    def enterFileName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#fileName.
#    def exitFileName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#functionName.
#    def enterFunctionName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#functionName.
#    def exitFunctionName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#indexName.
#    def enterIndexName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#indexName.
#    def exitIndexName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#languageName.
#    def enterLanguageName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#languageName.
#    def exitLanguageName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#libraryName.
#    def enterLibraryName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#libraryName.
#    def exitLibraryName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#localName.
#    def enterLocalName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#localName.
#    def exitLocalName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#mnemonicName.
#    def enterMnemonicName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#mnemonicName.
#    def exitMnemonicName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#paragraphName.
#    def enterParagraphName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#paragraphName.
#    def exitParagraphName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#procedureName.
#    def enterProcedureName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#procedureName.
#    def exitProcedureName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#programName.
#    def enterProgramName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#programName.
#    def exitProgramName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#recordName.
#    def enterRecordName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#recordName.
#    def exitRecordName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#reportName.
#    def enterReportName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#reportName.
#    def exitReportName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#routineName.
#    def enterRoutineName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#routineName.
#    def exitRoutineName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#screenName.
#    def enterScreenName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#screenName.
#    def exitScreenName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#sectionName.
#    def enterSectionName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#sectionName.
#    def exitSectionName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#systemName.
#    def enterSystemName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#systemName.
#    def exitSystemName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#symbolicCharacter.
#    def enterSymbolicCharacter(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#symbolicCharacter.
#    def exitSymbolicCharacter(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#textName.
#    def enterTextName(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#textName.
#    def exitTextName(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#cobolWord.
#    def enterCobolWord(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#cobolWord.
#    def exitCobolWord(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#literal.
#    def enterLiteral(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#literal.
#    def exitLiteral(self, ctx):
#        import pdb; pdb.set_trace()
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#booleanLiteral.
#    def enterBooleanLiteral(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#booleanLiteral.
#    def exitBooleanLiteral(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#numericLiteral.
#    def enterNumericLiteral(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#numericLiteral.
#    def exitNumericLiteral(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#integerLiteral.
#    def enterIntegerLiteral(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#integerLiteral.
#    def exitIntegerLiteral(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#cicsDfhRespLiteral.
#    def enterCicsDfhRespLiteral(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#cicsDfhRespLiteral.
#    def exitCicsDfhRespLiteral(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#cicsDfhValueLiteral.
#    def enterCicsDfhValueLiteral(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#cicsDfhValueLiteral.
#    def exitCicsDfhValueLiteral(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#figurativeConstant.
#    def enterFigurativeConstant(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#figurativeConstant.
#    def exitFigurativeConstant(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#specialRegister.
#    def enterSpecialRegister(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#specialRegister.
#    def exitSpecialRegister(self, ctx):
#        pass
#
#
#    # Enter a parse tree produced by Cobol85Parser#commentEntry.
#    def enterCommentEntry(self, ctx):
#        pass
#
#    # Exit a parse tree produced by Cobol85Parser#commentEntry.
#    def exitCommentEntry(self, ctx):
#        pass
#
#
