#!/usr/bin/env python

import string

##########################################################################################
# word_freq.py
#
# To run:
# python word_freq.py
#
# Purpose:
# Given a series of texts corresponding to different authors, create a list of the top
# unique words for each author to aid in predicting their word usage
#
# Input:
# books in text format, where the works of an author are in a single file
# (look for files with {author}_{title}.txt suffix)
# 
# Output:
# a file for each author which corresponds to the words that are unique in their writing
# (look for files with {author}__unique_words_output suffix)
#
#
# Algorithm:
# STEP1) Process each author and create a separate dict listing all of the words and their freq count
#        NOTE: ignore the list_stop_words[] because of their low value of predictability 
#
# STEP2) Combine all of the dicts into a single master_dict, the value is the sum of all
#        the occurences across all of the authors 
#
# STEP3) For each author, scan through the master_dict and identify the words that are
#        unique to that author
#
# STEP4) Print out top 500 unique words according to highest frequence for each author in 
#        a separate file {author}__unique_words_output.
#        NOTE: The top 500 words is controlled by the LIMIT variable
#
#
#########################################################################################


LIMIT = 500

list_stop_words = ["the", "and", "a", "is", "i", "am", "he", "she", "or", "they", "are", "of", "in", "it", "not", "with", "after", "have", "been", "to", "be", "as", "his", "was" "that", "then", "for", "him", "on", "from", "by", "had", "when", "one", "this", "at", "no", "my", "but", "who", "them", "me", "all", "were", "so", "their", "did", "would", "there", "has", "an", "any", "if", "should", "will", "some", "where", "we", "was", "that", "her", "you", "what", "said", "do", "said", "now", "you", "do", "up", "go", "one", "two", "go"]

def scan_docs(filename):

    word_dict = {}

    #scan doc to build dict
    with open(filename, 'r') as f:
        for line in f:
            #remove punctuation
            for c in string.punctuation:
                line = line.replace(c,"")
            for word in line.split():
                word = word.lower()
                #remove stop words
                if word in list_stop_words:
                    pass 
                #elsif word.isdigit():
                #    pass
                else:
                    if word in word_dict:
                        word_dict[word] += 1
                    else:
                        word_dict[word] = 1

    return(word_dict)


def add_to_master_dict(author_dict, master_dict):
    author_keylist = author_dict.keys()
    author_keylist.sort()
    for key in author_keylist:
        print "%s: %s" % (key, author_dict[key])
        if key in master_dict:
            master_dict[key] += author_dict[key]
        else:
            master_dict[key] = author_dict[key]


def print_unique_dict_keys(filename, author_dict, master_dict):
    
    count = 0
    output_filename = filename + "__unique_words_output"
    fo = open(output_filename, 'w')
    for author_key, value in sorted(author_dict.iteritems(), key=lambda (k,v): (v,k), reverse=True):
        if author_key in master_dict:
            #fo.write("for key %s, author_dict val = %d, and master_dict val = %d\n" % (author_key, author_dict[author_key], master_dict[author_key]))
            if author_dict[author_key] == master_dict[author_key]:
                count += 1
                if count < LIMIT:
                    fo.write("%s\n" % (author_key))
          


#    count = 0
#    output_filename = filename + "_output"
#    fo = open(output_filename, 'w')
#    for key, value in sorted(word_dict.iteritems(), key=lambda (k,v): (v,k), reverse=True):
#        #print "%s: %s" % (key, value) 
#        count += 1
#        if count < LIMIT:
#            fo.write("%s: %s\n" % (key, value)) 
#        else:
#            break
#


#scan these docs
master_dict = {}



EdgarRiceBurroughs_dict = scan_docs("./EdgarRiceBurroughs_all.txt")
add_to_master_dict(EdgarRiceBurroughs_dict, master_dict)

#for key, value in sorted(EdgarRiceBurroughs_dict.iteritems(), key=lambda (k,v): (v,k), reverse=True):
#    print "EdgarRiceBurroughs_dict %s: %s" % (key, value)

JackLondon_dict = scan_docs("./JackLondon_TheCalloftheWild.txt")
add_to_master_dict(JackLondon_dict, master_dict)

RichardHardingDavis_dict = scan_docs("./RichardHardingDavis_all.txt")
add_to_master_dict(RichardHardingDavis_dict, master_dict)

GKChesterton_dict = scan_docs("./GKChesterton_all.txt")
add_to_master_dict(GKChesterton_dict, master_dict)

JosephConrad_dict = scan_docs("./JosephConrad_all.txt")
add_to_master_dict(JosephConrad_dict, master_dict)

HenryJames_dict = scan_docs("./HenryJames_all.txt")
add_to_master_dict(HenryJames_dict, master_dict)

MarkTwain_dict = scan_docs("./MarkTwain_all.txt")
add_to_master_dict(MarkTwain_dict, master_dict)

AndrewBartonBanjoPaterson_dict = scan_docs("./AndrewBartonBanjoPaterson_TheManfromSnowyRiver.txt")
add_to_master_dict(AndrewBartonBanjoPaterson_dict, master_dict)

ArthurConanDoyle_dict = scan_docs("./ArthurConanDoyle_TheReturnofSherlockHolmes.txt")
add_to_master_dict(ArthurConanDoyle_dict, master_dict)

BaronessOrczy_dict = scan_docs("./BaronessOrczy_TheScarletPimpernel.txt")
add_to_master_dict(BaronessOrczy_dict, master_dict)

BoothTarkington_dict = scan_docs("./BoothTarkington_Penrod.txt")
add_to_master_dict(BoothTarkington_dict, master_dict)

DavidHerbertLawrence_dict = scan_docs("./DavidHerbertLawrence_SonsandLovers.txt")
add_to_master_dict(DavidHerbertLawrence_dict, master_dict)

ElbertHubbard_dict = scan_docs("./ElbertHubbard_JohnJacobAstor.txt")
add_to_master_dict(ElbertHubbard_dict, master_dict)

FrankNorris_dict = scan_docs("./FrankNorris_Blix.txt")
add_to_master_dict(FrankNorris_dict, master_dict)

FrederickDouglass_dict = scan_docs("./FrederickDouglass_MyBondageandMyFreedom.txt")
add_to_master_dict(FrederickDouglass_dict, master_dict)

GeorgeBorrow_dict = scan_docs("./GeorgeBorrow_TheBibleinSpain.txt")
add_to_master_dict(GeorgeBorrow_dict, master_dict)

GeorgeMacDonald_dict = scan_docs("./GeorgeMacDonald_AttheBackoftheNorthWind.txt")
add_to_master_dict(GeorgeMacDonald_dict, master_dict)

HarrietBeecherStowe_dict = scan_docs("./HarrietBeecherStowe_UncleTomsCabin.txt")
add_to_master_dict(HarrietBeecherStowe_dict, master_dict)

HenryDavidThoreau_dict = scan_docs("./HenryDavidThoreau_OntheDutyofCivilDisobedience.txt")
add_to_master_dict(HenryDavidThoreau_dict, master_dict)

HenryLawson_dict = scan_docs("./HenryLawson_IntheDaysWhentheWorldWasWideandOtherVerses.txt")
add_to_master_dict(HenryLawson_dict, master_dict)

JackLondon_dict = scan_docs("./JackLondon_TheCalloftheWild.txt")
add_to_master_dict(JackLondon_dict, master_dict)

JohnFox_dict = scan_docs("./JohnFox_HellferSartainandOtherStories.txt")
add_to_master_dict(JohnFox_dict, master_dict)

JohnGoodwin_dict = scan_docs("./JohnGoodwin_Email101.txt")
add_to_master_dict(JohnGoodwin_dict, master_dict)

JohnMilton_dict = scan_docs("./JohnMilton_ParadiseRegained.txt")
add_to_master_dict(JohnMilton_dict, master_dict)

LFrankBaum_dict = scan_docs("./LFrankBaum_TheWonderfulWizardofOz.txt")
add_to_master_dict(LFrankBaum_dict, master_dict)

LaoTze_dict = scan_docs("./LaoTze_TaoTehKing.txt")
add_to_master_dict(LaoTze_dict, master_dict)

LewisCarroll_dict = scan_docs("./LewisCarroll_all.txt")
add_to_master_dict(LewisCarroll_dict, master_dict)

LucyMaudMontgomery_dict = scan_docs("./LucyMaudMontgomery_all.txt")
add_to_master_dict(LucyMaudMontgomery_dict, master_dict)

NathanielHawthorne_dict = scan_docs("./NathanielHawthorne_TheHouseoftheSevenGables.txt")
add_to_master_dict(NathanielHawthorne_dict, master_dict)

NormanCoombs_dict = scan_docs("./NormanCoombs_TheBlackExperienceinAmerica.txt")
add_to_master_dict(NormanCoombs_dict, master_dict)

NormanFJoly_dict = scan_docs("./NormanFJoly_TheDawnofAmateurRadiointheUKandGreece.txt")
add_to_master_dict(NormanFJoly_dict, master_dict)

PhillisWheatley_dict = scan_docs("./PhillisWheatley_ReligiousandMoralPoems.txt")
add_to_master_dict(PhillisWheatley_dict, master_dict)

PhillisWheatley_dict = scan_docs("./PhillisWheatley_ReligiousandMoralPoems.txt")
add_to_master_dict(PhillisWheatley_dict, master_dict)

ReneDescartes_dict = scan_docs("./ReneDescartes_ADiscourseonMethod.txt")
add_to_master_dict(ReneDescartes_dict, master_dict)

RichardJefferies_dict = scan_docs("./RichardJefferies_ThePageantofSummer.txt")
add_to_master_dict(RichardJefferies_dict, master_dict)

RobertService_dict = scan_docs("./RobertService_TheSpelloftheYukon.txt")
add_to_master_dict(RobertService_dict, master_dict)

SamuelSmiles_dict = scan_docs("./SamuelSmiles_IndustrialBiography.txt")
add_to_master_dict(SamuelSmiles_dict, master_dict)

SaraTeasdale_dict = scan_docs("./SaraTeasdale_HelenofTroyandOtherPoems.txt")
add_to_master_dict(SaraTeasdale_dict, master_dict)

SherwoodAnderson_dict = scan_docs("./SherwoodAnderson_Winesburg.txt")
add_to_master_dict(SherwoodAnderson_dict, master_dict)

StephenCrane_dict = scan_docs("./StephenCrane_TheRedBadgeofCourage.txt")
add_to_master_dict(StephenCrane_dict, master_dict)

ThomasHardy_dict = scan_docs("./ThomasHardy_APairofBlueEyes.txt")
add_to_master_dict(ThomasHardy_dict, master_dict)

Unknown_dict = scan_docs("./Unknown_AladdinandtheMagicLamp.txt")
add_to_master_dict(Unknown_dict, master_dict)

Various_AppreciationsofRichardHardingDavis_dict = scan_docs("./Various_AppreciationsofRichardHardingDavis.txt")
add_to_master_dict(Various_AppreciationsofRichardHardingDavis_dict, master_dict)

Various_TheMartinLutherKing_dict = scan_docs("./Various_TheMartinLutherKing.txt")
add_to_master_dict(Various_TheMartinLutherKing_dict, master_dict)

Virgil_dict = scan_docs("./Virgil_TheAeneid.txt")
add_to_master_dict(Virgil_dict, master_dict)

WEBDuBois_dict = scan_docs("./WEBDuBois_TheSoulsofBlackFolk.txt")
add_to_master_dict(WEBDuBois_dict, master_dict)

WSomersetMaugham_dict = scan_docs("./WSomersetMaugham_TheMoonandSixpence.txt")
add_to_master_dict(WSomersetMaugham_dict, master_dict)

WinnSchwartau_dict = scan_docs("./WinnSchwartau_TerminalCompromise.txt")
add_to_master_dict(WinnSchwartau_dict, master_dict)






for key, value in sorted(master_dict.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    print "master_dict %s: %s" % (key, value)


print_unique_dict_keys("EdgarRiceBurroughs", EdgarRiceBurroughs_dict, master_dict)

print_unique_dict_keys("JackLondon", JackLondon_dict, master_dict) 

print_unique_dict_keys("RichardHardingDavis", RichardHardingDavis_dict, master_dict)

print_unique_dict_keys("GKChesterton", GKChesterton_dict, master_dict)

print_unique_dict_keys("JosephConrad", JosephConrad_dict, master_dict)

print_unique_dict_keys("HenryJames", HenryJames_dict, master_dict)

print_unique_dict_keys("MarkTwain", MarkTwain_dict, master_dict)

print_unique_dict_keys("AndrewBartonBanjoPaterson", AndrewBartonBanjoPaterson_dict, master_dict)

print_unique_dict_keys("ArthurConanDoyle", ArthurConanDoyle_dict, master_dict)

print_unique_dict_keys("BaronessOrczy", BaronessOrczy_dict, master_dict)

print_unique_dict_keys("BoothTarkington", BoothTarkington_dict, master_dict)

print_unique_dict_keys("DavidHerbertLawrence", DavidHerbertLawrence_dict, master_dict)

print_unique_dict_keys("ElbertHubbard", ElbertHubbard_dict, master_dict)

print_unique_dict_keys("FrankNorris", FrankNorris_dict, master_dict)

print_unique_dict_keys("FrederickDouglass", FrederickDouglass_dict, master_dict)

print_unique_dict_keys("GeorgeBorrow", GeorgeBorrow_dict, master_dict)

print_unique_dict_keys("GeorgeMacDonald", GeorgeMacDonald_dict, master_dict)

print_unique_dict_keys("HarrietBeecherStowe", HarrietBeecherStowe_dict, master_dict)

print_unique_dict_keys("HenryDavidThoreau", HenryDavidThoreau_dict, master_dict)

print_unique_dict_keys("HenryLawson", HenryLawson_dict, master_dict)

print_unique_dict_keys("JohnFox_dict", JohnFox_dict, master_dict)

print_unique_dict_keys("JohnGoodwin", JohnGoodwin_dict, master_dict)

print_unique_dict_keys("JohnMilton", JohnMilton_dict, master_dict)

print_unique_dict_keys("LFrankBaum", LFrankBaum_dict, master_dict)

print_unique_dict_keys("LaoTze", LaoTze_dict, master_dict)

print_unique_dict_keys("LewisCarroll", LewisCarroll_dict, master_dict)

print_unique_dict_keys("LucyMaudMontgomery", LucyMaudMontgomery_dict, master_dict)

print_unique_dict_keys("NathanielHawthorne", NathanielHawthorne_dict, master_dict)

print_unique_dict_keys("NormanCoombs", NormanCoombs_dict, master_dict)

print_unique_dict_keys("NormanFJoly", NormanFJoly_dict, master_dict)

print_unique_dict_keys("PhillisWheatley", PhillisWheatley_dict, master_dict)

print_unique_dict_keys("ReneDescartes", ReneDescartes_dict, master_dict)

print_unique_dict_keys("RichardJefferies", RichardJefferies_dict, master_dict)

print_unique_dict_keys("RobertService", RobertService_dict, master_dict)

print_unique_dict_keys("SamuelSmiles", SamuelSmiles_dict, master_dict)

print_unique_dict_keys("SaraTeasdale", SaraTeasdale_dict, master_dict)

print_unique_dict_keys("SherwoodAnderson", SherwoodAnderson_dict, master_dict)

print_unique_dict_keys("StephenCrane", StephenCrane_dict, master_dict)

print_unique_dict_keys("ThomasHardy", ThomasHardy_dict, master_dict)

print_unique_dict_keys("Unknown", Unknown_dict, master_dict)

print_unique_dict_keys("Various_AppreciationsofRichardHardingDavis", Various_AppreciationsofRichardHardingDavis_dict, master_dict)

print_unique_dict_keys("Various_TheMartinLutherKing", Various_TheMartinLutherKing_dict, master_dict)

print_unique_dict_keys("Virgil", Virgil_dict, master_dict)

print_unique_dict_keys("WEBDuBois", WEBDuBois_dict, master_dict)

print_unique_dict_keys("WSomersetMaugham", WSomersetMaugham_dict, master_dict)

print_unique_dict_keys("WinnSchwartau", WinnSchwartau_dict, master_dict)





