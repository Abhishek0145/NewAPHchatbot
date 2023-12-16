from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGreet(Action):
    def name(self) -> Text:
        return "utter_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hey, I am FusionWizz, How can I help you?")
        return []

class ActionGoodbye(Action):
    def name(self) -> Text:
        return "utter_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Bye, have a nice day.")
        return []

class ActionBotChallenge(Action):
    def name(self) -> Text:
        return "utter_bot_challenge"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Sorry, Please ask me questions regarding APH Approval Process Handbook")
        return []

class ActionGeneralInfoVocationalEducation(Action):
    def name(self) -> Text:
        return "utter_general_info_vocational_education"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Vocational Education is occupation-based learning with practical training, directly developing expertise in specific skills. It differs from traditional education by focusing on job preparation and skill specialization.")
        return []

class ActionNSQF(Action):
    def name(self) -> Text:
        return "utter_nsqf"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="NSQF is a competency-based framework organizing qualifications into levels (1 to 10) based on knowledge, skills, and aptitude. It applies to formal, non-formal, or informal learning and ensures learners possess defined outcomes.")
        return []

class ActionAffiliationVocationalCourses(Action):
    def name(self) -> Text:
        return "utter_affiliation_vocational_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Vocational Courses may affiliate with existing universities, Skill Universities, or National Universities. Affiliation can also be with the Board of Technical Education, depending on the circumstances.")
        return []

class ActionDVocBVocProgrammes(Action):
    def name(self) -> Text:
        return "utter_d_voc_b_voc_programmes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="These programs provide Diploma/Undergraduate studies integrating specific job roles and their Qualification Packs/National Occupational Standards, along with a foundation in general education.")
        return []

class ActionRegulationFeesVocationalCourses(Action):
    def name(self) -> Text:
        return "utter_regulation_fees_vocational_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The fees for Vocational Courses are regulated by respective state bodies, Technical Boards, Universities, or relevant authorities depending on the jurisdiction.")
        return []

class ActionCreditBasedModularPrograms(Action):
    def name(self) -> Text:
        return "utter_credit_based_modular_programs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Modular programs have credits for skill and general education, allowing multiple exits and entries. Learners can seek employment after any award level and return to upgrade skills or qualifications as needed.")
        return []

class ActionCurriculumMixVocationalEducation(Action):
    def name(self) -> Text:
        return "utter_curriculum_mix_vocational_education"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The curriculum should have a suitable mix with 40% of total credits allocated to general education and the remaining 60% to skill development components.")
        return []

class ActionCurriculumApprovalOversight(Action):
    def name(self) -> Text:
        return "utter_curriculum_approval_oversight"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The curriculum details are approved by respective Technical Boards or Universities. Oversight is conducted by the Ministry of Education (MoE) or relevant authorities.")
        return []

class ActionRoleGeneralEducationComponent(Action):
    def name(self) -> Text:
        return "utter_role_general_education_component"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The General Education Component constitutes 40% of total credits, providing a balanced educational foundation alongside the specialized skill development components.")
        return []

class ActionEmphasisCreditBasedModularPrograms(Action):
    def name(self) -> Text:
        return "utter_emphasis_credit_based_modular_programs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Credit-based modular programs allow flexibility for learners, enabling them to enter the workforce at various award levels and return to upgrade qualifications or skills as needed.")
        return []

class ActionFocusSkillDevelopmentComponentDesign(Action):
    def name(self) -> Text:
        return "utter_focus_skill_development_component_design"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The skill development component should lead to comprehensive specialization in one or two domains, ensuring a thorough understanding of the selected job roles.")
        return []

class ActionNationalOccupationalStandards(Action):
    def name(self) -> Text:
        return "utter_national_occupational_standards"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="In such cases, the university/college should collaborate with industry experts to develop the curriculum for the specific area or job role.")
        return []

class ActionCurriculumEmphasisWorkReadinessSkills(Action):
    def name(self) -> Text:
        return "utter_curriculum_emphasis_work_readiness_skills"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The curriculum should focus on developing work-ready skills in each of the three years, including practical work, on-the-job training, student portfolios, and project work.")
        return []

class ActionDeterminingGeneralEducationComponent(Action):
    def name(self) -> Text:
        return "utter_determining_general_education_component"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The Board of Studies of the affiliating University/Board decides the general education component, adhering to normal university standards. It includes holistic development courses, support to core trade, soft skills, IT skills, and language proficiency.")
        return []

class ActionCompletingSkillModulesAcquiringCredits(Action):
    def name(self) -> Text:
        return "utter_completing_skill_modules_acquiring_credits"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Students complete skill modules at various certification levels, acquiring necessary credits from Skill Knowledge Providers (SKP), Training Providers, or Sector Skill Councils approved by NSDC or relevant authorities.")
        return []

class ActionCreditTransferCertification(Action):
    def name(self) -> Text:
        return "utter_credit_transfer_certification"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Credits, including skill and education components, are transferred to the Technical Board or University. If the required credits for a certification level are met, the Technical Board or University awards the certification.")
        return []

class ActionCertificationLevelsInformation(Action):
    def name(self) -> Text:
        return "utter_certification_levels_information"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="All certification levels are identified in Appendix 1 of the document. Specific details can be referred to in the SAMVAY Document accessible at: SAMVAY Document.")
        return []

class ActionGeneralStreamToVocationalStreamTransition(Action):
    def name(self) -> Text:
        return "utter_general_stream_to_vocational_stream_transition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="A student can enter at a certain level, provided the required skills are acquired from a registered SKP/Training Provider. Institutions may offer bridge courses for necessary knowledge transfer for those seeking lateral entry.")
        return []

class ActionMovementBetweenVocationalAndFormalHigherEducationStreams(Action):
    def name(self) -> Text:
        return "utter_movement_between_vocational_and_formal_higher_education_streams"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Candidates have the freedom to move between Vocational and formal higher education streams at various stages, including multi-level entry and exit systems, subject to fulfilling the required criteria of the affiliating body.")
        return []

class ActionNOCProcess(Action):
    def name(self) -> Text:
        return "utter_noc_process"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The institution must apply online on the AICTE Web-Portal as per the calendar of AICTE for seeking NOC (No Objection Certificate).")
        return []

class ActionPrerequisitesForEstablishingTechnicalInstitution(Action):
    def name(self) -> Text:
        return "utter_prerequisites_for_establishing_technical_institution"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The new technical institution should meet the infrastructure requirements outlined in the Approval Process Handbook. Additionally, it should have prior approval from the Council before offering any technical courses.")
        return []

class ActionSignificanceOfAdheringToLaws(Action):
    def name(self) -> Text:
        return "utter_significance_of_adhering_to_laws"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The institution must adhere to existing Central, State, and Local Laws, along with norms from other Regulatory Bodies if applicable, in order to ensure compliance and legality in its establishment and operation.")
        return []

class ActionRoleOfStateGovernmentInEstablishment(Action):
    def name(self) -> Text:
        return "utter_role_of_state_government_in_establishment"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The State Government/UT is expected to provide financial assistance for the establishment of technical institutions offering engineering and technology programs at DIPLOMA/UG/PG levels. The government should have a budget provision of at least ₹100 lakh and provide the necessary land.")
        return []

class ActionAICTEHandlingApplications(Action):
    def name(self) -> Text:
        return "utter_AICTE_handling_applications"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("AICTE notifies the application process through Public Notices and its website, setting cut-off dates for various categories. The application process is conducted online through the AICTE Web Portal using the National Single Window System (NSWS). Offline applications are not accepted.")
        return []

class ActionTimeFrameForSubmissionAndConsequences(Action):
    def name(self) -> Text:
        return "utter_time_frame_for_submission_and_consequences"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("AICTE specifies a time schedule through Public Notices and its website for the submission of applications. It is mandatory for applications to be submitted on the AICTE Web Portal through NSWS, with both the application and payment made by the last date as notified in the Public Notice/AICTE Website. Applications submitted after the deadline will not be accepted.")
        return []

class ActionTypesOfProgramsForApproval(Action):
    def name(self) -> Text:
        return "utter_types_of_programs_for_approval"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("A new technical institution can seek approval to offer programs in Engineering and Technology, Planning, Applied Arts and Crafts, Design, Hotel Management and Catering Technology (Diploma/Undergraduate Degree Level), Computer Application (MCA), and Management (Post Graduate Certificate/Post Graduate Diploma/Post Graduate Degree Level).")
        return []

class ActionEligibilityCriteriaForPromoters(Action):
    def name(self) -> Text:
        return "utter_eligibility_criteria_for_promoters"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Promoters can be a Society registered under the Societies Registration Act, 1860, a Trust registered under the Indian Trust Act, 1882, a Company established under Section 8 of the Companies Act, 2013, or the Central/State Government/UT Administration. Foreign equity in a company applying for the establishment of a technical institution is generally not permitted.")
        return []

class ActionIneligibilityOfCertainPrograms(Action):
    def name(self) -> Text:
        return "utter_ineligibility_of_certain_programs"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("New institutions are not eligible for these programs as per section 1.3.3. The specific reasons for this exclusion are not provided in the given content.")
        return []

class ActionMinistryOfEducationSchemesForEstablishment(Action):
    def name(self) -> Text:
        return "utter_Ministry_of_Education_schemes_for_establishment"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The schemes mentioned are the 'Sub-Mission on Polytechnics' and initiatives for educationally backward districts/left-wing extremism affected areas. The concerned State Government/UT must apply online on the AICTE Web Portal, and the application will go through scrutiny committees before approval.")
        return []

class ActionConsequencesOfNotShiftingLocation(Action):
    def name(self) -> Text:
        return "utter_consequences_of_not_shifting_location"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("If an institution does not shift to the permanent location within 2 years, and if it meets the norms, the 'Approved Intake' in the course(s) shall be reduced to 50%. If the institution has not shifted even after 4 years, the Council will take appropriate action.")
        return []

class ActionExistingInstitutionsApprovalByAICTE(Action):
    def name(self) -> Text:
        return "utter_existing_institutions_approval_by_AICTE"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Existing institutions can seek approval from AICTE for the first time if they offer courses in Applied Arts and Crafts/Vocational (Technical) without AICTE approval or if they are non-technical institutions already running MBA/MCA courses without AICTE approval.")
        return []

class ActionAdditionalChargesForExtraCommittees(Action):
    def name(self) -> Text:
        return "utter_additional_charges_for_extra_committees"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("For an additional Scrutiny Committee, the applicant has to remit ₹0.55 Lakh, and for an additional Expert Visit Committee (Online/Offline), the applicant has to remit ₹1.10 Lakh or ₹2.20 Lakh, respectively, as additional TER Charges.")
        return []

class ActionConsequencesOfNotPayingTERWithinDeadline(Action):
    def name(self) -> Text:
        return "utter_consequences_of_not_paying_TER_within_deadline"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("If the TER Charges are not paid within the deadline, the application shall not be considered.")
        return []
    
class ActionImportanceOfOnlineApplicationThroughNSWS(Action):
    def name(self) -> Text:
        return "utter_importance_of_online_application_through_NSWS"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Institutions seeking approval for the first time must submit an online application through NSWS on the AICTE web portal to be considered for processing.")
        return []

class ActionAICTEHandlingRefundOrExcessPayment(Action):
    def name(self) -> Text:
        return "utter_AICTE_handling_refund_or_excess_payment"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("In case of eligible refund or excess payment, the amount shall be refunded to the applicant after processing.")
        return []
    
class ActionUserIDAllotmentAndAssociatedCost(Action):
    def name(self) -> Text:
        return "utter_USER_ID_allotment_and_associated_cost"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The USER ID with a password is allotted upon payment of ₹5500 through the payment gateway on AICTE Web-Portal. This unique identifier allows applicants to track the status of their application.")
        return []

class ActionProcedureForPasswordRecoveryAndCharges(Action):
    def name(self) -> Text:
        return "utter_procedure_for_password_recovery_and_charges"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("If an existing institution forgets its password, it can apply online for a new one by remitting ₹5500 as Technical Education Regulatory (TER) Charges through the payment gateway on AICTE Web-Portal.")
        return []

class ActionTERChargesCalculationAndAnnualIncrease(Action):
    def name(self) -> Text:
        return "utter_TER_charges_calculation_and_annual_increase"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("TER Charges vary based on the type of institution. For Minority Institution/Institution in specific regions, it is ₹6.60 Lakh, for Government/Government Aided Institutions/PPP mode, it is Nil, and for all other institutions, it is ₹8.80 Lakh. The annual increase is 10%.")
        return []
    
class ActionEligibilityForTERChargeRefund(Action):
    def name(self) -> Text:
        return "utter_eligibility_for_TER_charge_refund"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Applications submitted under Clause 1.3.1 and 1.3.5, if rejected at the level of Scrutiny/Re-Scrutiny without availing the appeal provision, are eligible for a refund of TER Charges after a deduction of ₹0.55 Lakh.")
        return []

class ActionPrecautionsForDataEntryAndSubmission(Action):
    def name(self) -> Text:
        return "utter_precautions_for_data_entry_and_submission"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Applicants should ensure that the data entered in their online application is correct. They can edit the data until the final submission, after which no further editing is allowed. All documents should be digitally signed, and applicants should exercise caution before pressing the 'SUBMIT' tab.")
        return []

class ActionSignificanceOfDigitalSignatureCertificate(Action):
    def name(self) -> Text:
        return "utter_significance_of_Digital_Signature_Certificate"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Institutions are required to submit applications with a DSC to ensure the authenticity of the documents. Any document uploaded without a Digital Signature will not be considered valid.")
        return []

class ActionSignificanceOfAffidavit2AndConsequencesOfFalseInfo(Action):
    def name(self) -> Text:
        return "utter_significance_of_Affidavit_2_and_consequences_of_false_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Affidavit 2, sworn before a First Class Judicial Magistrate or Public Notary, is a legal declaration. In case of false information, AICTE may invoke civil and/or criminal provisions as per the regulations in place.")
        return []
    
class ActionMandatorySubmissionToStateGovernmentAndAffiliatingUniversity(Action):
    def name(self) -> Text:
        return "utter_mandatory_submission_to_State_Government_and_affiliating_University"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Submitting a copy to the State Government/UT and affiliating University/Board ensures transparency and allows these entities to provide their views on the application.")
        return []
    
class ActionTimelineForViewsFromStateGovernmentAndAffiliatingUniversity(Action):
    def name(self) -> Text:
        return "utter_timeline_for_views_from_State_Government_and_affiliating_University"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The State Government/UT and affiliating University/Board should forward their views on the application to the Approval Bureau of AICTE not later than one week from the last date specified for the submission of the application, as per the Public Notice/AICTE Web portal.")
        return []
    
class ActionLiftingOfMoratoriumForNewInstitutions(Action):
    def name(self) -> Text:
        return "utter_lifting_of_moratorium_for_new_institutions"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The lifting of the moratorium means that applications for establishing new institutions in Engineering and Technology will be considered, with a preference for those offering courses in multi-disciplinary areas in line with the National Education Policy (NEP) 2020 in STEM areas.")
        return []
    
class ActionRequirementsAndEligibilityForPromoterTrustSocietyCompany(Action):
    def name(self) -> Text:
        return "utter_requirements_and_eligibility_for_Promoter_Trust_Society_Company"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The Promoter Trust/Society/Company must have the land/built-up area required for the institution, with lawful possession and a clear title in its name on or before the date of submission of the application.")
        return []

class ActionMinimumFundsRequiredForProofOfOperationalExpenses(Action):
    def name(self) -> Text:
        return "utter_minimum_funds_required_for_proof_of_operational_expenses"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The minimum funds required for different programs are as follows:\nEngineering and Technology: ₹100 lakh\nPlanning: ₹50 lakh\nApplied Arts and Crafts: ₹50 lakh\nDesign: ₹50 lakh\nHotel Management and Catering Technology: ₹50 lakh\nComputer Application (MCA): ₹50 lakh\nManagement: ₹50 lakh")
        return []
    
class ActionBuildingPlanRequirementsAndApproval(Action):
    def name(self) -> Text:
        return "utter_building_plan_requirements_and_approval"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The building plan for the entire duration of the institution's programs must be prepared by an architect registered with the Council of Architecture or a licensed surveyor. The plan should be approved by the Competent Authority designated by the concerned State Government/UT.")
        return []

class ActionQualificationsRequiredForHeadOfTechnicalInstitution(Action):
    def name(self) -> Text:
        return "utter_qualifications_required_for_head_of_technical_institution"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The head of the technical institution should be named as the 'Principal/Director' and must have qualifications as per AICTE norms defined for a Principal in a program of the technical institution.")
        return []
    
class ActionExistingInstitutionsApplyingForClosureAndStartingNewInstitution(Action):
    def name(self) -> Text:
        return "utter_existing_institutions_applying_for_closure_and_starting_new_institution"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Yes, existing institutions applying for closure can also apply for starting a new technical institution in the same premises in the same academic year, provided they apply for progressive/complete closure of the existing program and a different program for the new institution.")
        return []

class ActionOutcomesOfApprovalUnderSection152a(Action):
    def name(self) -> Text:
        return "utter_outcomes_of_approval_under_section_1.5.2a"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("If the application is approved, the existing institution will be considered closed (progressive/complete closure, as applicable), and any liabilities arising out of this will solely be the responsibility of the Trust/Society/Company/Technical Institution.")
        return []

class ActionFundPositionRequirementsInTermsOfFDRsAndBankAccounts(Action):
    def name(self) -> Text:
        return "utter_fund_position_requirements_in_terms_of_FDRs_and_bank_accounts"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The fund position of the applicant should be in the form of FDRs and/or bank accounts in Nationalized Banks or Scheduled Commercial Banks recognized by the Reserve Bank of India on the date of scrutiny.")
        return []

class ActionRequirementsForGovernmentGovernmentAidedInstitutionsCentralStateUniversities(Action):
    def name(self) -> Text:
        return "utter_requirements_for_Government_Government-Aided_Institutions_Central_State_Universities"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("For Government/Government-Aided Institutions/Central/State Universities, the government must have a budget provision of a minimum of ₹100 lakh and the requisite land/built-up area for the establishment of a new institute.")
        return []

class ActionRestrictionsOnUseOfNamesForNewTechnicalInstitution(Action):
    def name(self) -> Text:
        return "utter_restrictions_on_use_of_names_for_new_technical_institution"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The abbreviated form of the name of the technical institution cannot become IIM/IIT/IISc/NIT/IISER/IIIT/IIEST/AICTE/UGC/MoE/GoI. The institution also cannot use the words Government/India/Indian/National/All India/All India Council/Commission in a way that implies it is a government institute, unless established by the Government of India.")
        return []

class ActionDifferentiationOfExistingInstitutionsWithSameNameWithinState(Action):
    def name(self) -> Text:
        return "utter_differentiation_of_existing_institutions_with_same_name_within_state"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Existing institutions with the same name within a state should at least add the name of the Village/Town/City where they are located as an integral part of the institution's name.")
        return []
    





class Actiongovernmentsupportpublicuniversities(Action):
    def name(self) -> Text:
        return "utter_government_support_public_universities"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Public Universities in India receive support from both the Government of India and the respective State Governments. Private Universities are primarily supported by various trusts and societies.")
        return []

class Actionprivateuniversitiessupport(Action):
    def name(self) -> Text:
        return "utter_private_universities_support"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Private Universities in India are mostly supported by various trusts and societies.")
        return []

class Actionuniversityrecognitionregulatorybody(Action):
    def name(self) -> Text:
        return "utter_university_recognition_regulatory_body"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Universities in India are recognized by the University Grants Commission (UGC), in accordance with the UGC Act, 1956.")
        return []

class Actioncentralvsstateuniversities(Action):
    def name(self) -> Text:
        return "utter_central_vs_state_universities"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text='Central Universities in India are established by an Act of Parliament and fall under the purview of the Ministry of Education (MoE). State Universities are run by the concerned State Government/Union Territories and are established by an Act enacted by the legislative assembly of the respective State/UT. A University may also have a "Constituent College," which is an Institution/Department/College/School as a part of the University.')
        return []

class Actionconstituentcollegesignificance(Action):
    def name(self) -> Text:
        return "utter_constituent_college_significance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="A \"Constituent College\" in the context of a University in India refers to an Institution/Department/College/School that is a part of the University.")
        return []

class Actiondeemeduniversitydeclarationprocess(Action):
    def name(self) -> Text:
        return "utter_deemed_university_declaration_process"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Institutions Deemed to be University are Institutions for Higher Education declared on the recommendations of the University Grants Commission by the Central Government, under Section 3 of the UGC Act.")
        return []

class Actionstateprivateuniversitiescharacteristic(Action):
    def name(self) -> Text:
        return "utter_state_private_universities_characteristic"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="State Private Universities in India are established by the State, recognized by the UGC, and supported by various trusts and societies.")
        return []

class ActiontechnicaluniversitiesAICTEnorms(Action):
    def name(self) -> Text:
        return "utter_technical_universities_aicte_norms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Technical Universities offering Technical Program/Courses at all levels are required to maintain norms and standards related to infrastructure, faculty, and other criteria as specified by AICTE in the Approval Process Handbook and any additional norms prescribed by relevant statutory bodies.")
        return []

class ActionAICTEinspectionmandate(Action):
    def name(self) -> Text:
        return "utter_aicte_inspection_mandate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The AICTE Act, 1987 Clause-11 mandates the Council to conduct inspections to ensure that a University is maintaining the norms and standards of teaching, examination, and research.")
        return []

class ActionAICTEapprovalapplicationprocess(Action):
    def name(self) -> Text:
        return "utter_aicte_approval_application_process"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Central/State and Private Universities can apply for AICTE's approval by submitting online applications with requisite details of infrastructure, land, faculty, etc., as specified in the AICTE Approval Process Handbook. Additionally, they must fulfill UGC norms and adhere to existing Central, State, and Local Laws.")
        return []

class Actionjurisdictionapprovalauthority(Action):
    def name(self) -> Text:
        return "utter_jurisdiction_approval_authority"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The area of jurisdiction for State Universities/Private Universities/Institutions Deemed to be Universities (including off-campuses) is approved by the UGC/State jurisdiction.")
        return []

class Actionadmissionrestrictionsdeemeduniversities(Action):
    def name(self) -> Text:
        return "utter_admission_restrictions_deemed_universities"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Institutions Deemed to be Universities offering Technical Course(s)/Programme(s) are not allowed to admit students without the prior approval of the Council.")
        return []

class ActionExtensionApprovalCriteria(Action):
    def name(self) -> Text:
        return "utter_extension_approval_criteria"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Existing Universities/Institutions Deemed to be University can be eligible for a 3-year Extension of Approval (EoA) by meeting any one of the following criteria:\n"
                                      "i. Figuring in the 8th Edition of NIRF ranked Institutions (announcement made in 5th June 2023).\n"
                                      "ii. Figuring in QS World Ranking Asia-2024 (announcement made on 8th Nov 2023).\n"
                                      "iii. Universities/Institutions Deemed to be University having a minimum of 30% eligible courses in regular mode with NBA accreditation valid till 30th April 2025. (The institutions should continue to get accreditation for their programs).\n"
                                      "iv. Universities/Institutions Deemed to be University with a valid NAAC score of 3.01 and above on a scale of 4.0.\n"
                                      "v. Universities/Institutions Deemed to be University having conferred 'Autonomous Status' by UGC.\n"
                                      "vi. Universities/Institutions Deemed to be University having more than 80% admissions in all the courses/programs offered consecutively for the last 5 Academic Years.\n")

        return []

class ActionAICTEapprovalannualdatarequirement(Action):
    def name(self) -> Text:
        return "utter_aicte_approval_annual_data_requirement"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Although Universities/Institutions Deemed to be University can receive an extended EoA for 3 years, they are required to submit information/data annually during the AICTE Approval Process for the respective years.")
        return []

class ActionAICTEprocessingschedulenotification(Action):
    def name(self) -> Text:
        return "utter_aicte_processing_schedule_notification"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="AICTE notifies the time schedule for processing applications through a Public Notice in leading newspapers and on the AICTE Website from time to time. The time schedule mentioned in the Public Notice/AICTE Website is considered final and binding.")
        return []

class Actionuniversityapprovalrequestrequirement(Action):
    def name(self) -> Text:
        return "utter_university_approval_request_requirement"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="To process any request from universities regarding approval, online application submission is mandatory. Applications submitted offline are not accepted.")
        return []

class ActionAICTEapplicationinvitationchannels(Action):
    def name(self) -> Text:
        return "utter_aicte_application_invitation_channels"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="AICTE uses leading newspapers and the AICTE Website to notify through a Public Notice, inviting applications along with cut-off dates for various categories and processing thereof.")
        return []

class ActionAICTEapplicationdeadline(Action):
    def name(self) -> Text:
        return "utter_aicte_application_deadline"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Yes, the submission of an application on the AICTE Web-Portal and payment shall not be later than the last date as notified in the Public Notice/AICTE Website.")
        return []

class Actionapplicationprocesshandbookscope(Action):
    def name(self) -> Text:
        return "utter_application_process_handbook_scope"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The application process covers Universities offering Technical Programme(s) at Diploma/Post Diploma Certificate/Under Graduate Degree/Post Graduate Diploma/Post Graduate Degree Level for conducting Programs in Engineering and Technology, Planning, Applied Arts, Crafts and Design, Hotel Management and Catering Technology, MCA, and Management.")
        return []

class Actiontechnicalprogramlevelscovered(Action):
    def name(self) -> Text:
        return "utter_technical_program_levels_covered"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The application process covers Technical Programme(s) at various levels, including Diploma, Post Diploma Certificate, Under Graduate Degree, Post Graduate Diploma, and Post Graduate Degree.")
        return []

class Actionacademicdisciplinescovered(Action):
    def name(self) -> Text:
        return "utter_academic_disciplines_covered"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The programs covered by the application process span across Engineering and Technology, Planning, Applied Arts, Crafts and Design, Hotel Management and Catering Technology, MCA, and Management.")
        return []

class Actionspecificcategoriesapprovalhandbook(Action):
    def name(self) -> Text:
        return "utter_specific_categories_approval_handbook"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Yes, specific categories are mentioned in Chapter I, II, and III of the Approval Process Handbook for Universities offering Technical Programme(s).")
        return []

class Actionprogramfocusapprovalprocess(Action):
    def name(self) -> Text:
        return "utter_program_focus_approval_process"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The programs included in the application process primarily focus on Engineering and Technology, Planning, Applied Arts, Crafts and Design, Hotel Management and Catering Technology, MCA, and Management.")
        return []

class ActionAICTEprocessingschedulecommunication(Action):
    def name(self) -> Text:
        return "utter_aicte_processing_schedule_communication"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("AICTE communicates the time schedule for processing applications through Public Notices in leading newspapers and on the AICTE Website from time to time.")
        return []

class Actionuniversityapprovalrequestmandatoryrequirement(Action):
    def name(self) -> Text:
        return "utter_university_approval_request_mandatory_requirement"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The mandatory requirement for processing approval requests from Universities is the submission of online applications. Offline applications are not accepted.")
        return []

class Actiontechnicalprogramdisciplinesfocus(Action):
    def name(self) -> Text:
        return "utter_technical_program_disciplines_focus"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The programs covered by the application process focus on various academic disciplines, including Engineering and Technology, Planning, Applied Arts, Crafts and Design, Hotel Management and Catering Technology, MCA, and Management.")
        return []

class Actioneligibilitycriteriauniversities(Action):
    def name(self) -> Text:
        return "utter_eligibility_criteria_universities"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Yes, specific eligibility criteria are mentioned in Chapter I, II, and III of the Approval Process Handbook for Universities offering Technical Programme(s).")
        return []

class Actiontechnicalprogramlevelsinapplicationprocess(Action):
    def name(self) -> Text:
        return "utter_technical_program_levels_in_application_process"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The application process considers Technical Programme(s) at various levels, including Diploma, Post Diploma Certificate, Under Graduate Degree, Post Graduate Diploma, and Post Graduate Degree.")
        return []

class Actionmultiplecampusesapprovalprocess(Action):
    def name(self) -> Text:
        return "utter_multiple_campuses_approval_process"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("A University with Multiple Campuses/Off Campuses/Constituent Colleges can choose to apply separately for approval for each campus/off-campus/constituent college. Alternatively, they can apply as a single entity with all their courses and programs of both Main and Off-campus.")
        return []

class Actionpermitteduniversitycoursesnomenclatures(Action):
    def name(self) -> Text:
        return "utter_permitted_university_courses_nomenclatures"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("All Universities (Central/State Government/State Private) and Category-I&II Deemed to be University are permitted to run courses/programs with nomenclatures prescribed in AICTE APH.")
        return []

class Actiondirectivecentralstateprivateuniversities(Action):
    def name(self) -> Text:
        return "utter_directive_central_state_private_universities"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Central/State/Private Universities interested in obtaining AICTE approval must obtain approval for all Technical Programme(s)/Course(s)/intake and not just for selected ones. This ensures clarity and eliminates confusion for students.")
        return []

class ActiondirectivedeemeduniversitiesAICTEapproval(Action):
    def name(self) -> Text:
        return "utter_directive_deemed_universities_aicte_approval"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Institutions Deemed to be Universities are mandated to have AICTE approval from the Academic Year 2018-19, as per the Hon’ble Supreme Court Order dated 03-11-2017. It is mandatory to obtain AICTE approval before running any Technical Programme(s)/Course(s).")
        return []

class Actionnormsstandardsrequirementuniversities(Action):
    def name(self) -> Text:
        return "utter_norms_standards_requirement_universities"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("State Public & Private Universities and Central Universities are required to maintain Norms & Standards as specified in APH from time to time. They shall take AICTE approval for regular courses falling under the purview of the council, especially if the same courses are to be offered in ODL/OL mode, as per UGC Regulation.")
        return []

class Actionpartialapprovalpermittingconditions(Action):
    def name(self) -> Text:
        return "utter_partial_approval_permitting_conditions"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("No, the application for partial approval of any Programme(s)/Course(s)/Intake at any level is NOT permitted.")
        return []

class ActionuserIDpasswordapprovalprocess(Action):
    def name(self) -> Text:
        return "utter_user_id_password_approval_process"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("USER ID and Password are crucial credentials for accessing and navigating the AICTE Web-Portal during the approval process.")
        return []

class ActionTERchargesdefinition(Action):
    def name(self) -> Text:
        return "utter_ter_charges_definition"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("TER Charges are fees associated with the approval process. Existing Universities offering Technical Programme(s) at various levels are required to pay TER Charges, and the charges vary based on the type of university.")
        return []
    
class ActionTERchargesstructurefirstapproval(Action):
    def name(self) -> Text:
        return "utter_ter_charges_structure_first_approval"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The TER Charges structure for existing universities applying for approval for the first time varies based on the type of university.")
        return []

class ActionTERchargesapplicabilitymainoffcampus(Action):
    def name(self) -> Text:
        return "utter_ter_charges_applicability_main_off_campus"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Yes, separate TER Charges are applicable for main and off-campus, as approved by UGC")
        return []
    
class ActionannualincreaseTERcharges(Action):
    def name(self) -> Text:
        return "utter_annual_increase_ter_charges"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Yes, there is an annual increase of 10% in TER Charges.")
        return []

class ActioncircumstancesadditionalTERcharges(Action):
    def name(self) -> Text:
        return "utter_circumstances_additional_ter_charges"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Additional TER Charges may be required in extraordinary circumstances, such as conducting additional online Scrutiny Committee, Standing Hearing Committee, Standing Appellate Committee, or Expert Visit Committee.")
        return []

class ActionadditionalTERchargespayment(Action):
    def name(self) -> Text:
        return "utter_additional_ter_charges_payment"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Additional TER Charges should be remitted through the AICTE payment gateway on the AICTE Web-Portal within the specified deadline. Failure to do so will result in the application not being considered.")
        return []
    
class ActionAICTEapprovalapplicationsubmission(Action):
    def name(self) -> Text:
        return "utter_aicte_approval_application_submission"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Applicants shall submit the application on the AICTE Web-Portal @ www.aicte-india.org on or before the last date, as mentioned in the Public Notice/AICTE Website, and this is mandatory.")
        return []

class Actionapplicationdataeditingprovision(Action):
    def name(self) -> Text:
        return "utter_application_data_editing_provision"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Yes, there is a facility to edit the data until the submission of the application. After submission, the modification of data shall not be allowed until the processing of the application is completed.")
        return []

class Actionimportanceofcutoffdatesubmission(Action):
    def name(self) -> Text:
        return "utter_importance_of_cut_off_date_submission"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Applications complete in all respects and submitted (including payment) within the cut-off date, as mentioned in the Public Notice/AICTE Website, shall only be considered for processing as per the norms and procedures specified in the Approval Process Handbook.")
        return []

class Actionaffidavitrequirementapplicationprocess(Action):
    def name(self) -> Text:
        return "utter_affidavit_requirement_application_process"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("An Affidavit sworn before the First Class Judicial Magistrate or Notary or an Oath Commissioner on Rs. 100/- Non-Judicial stamp paper/e-stamp paper shall be Digitally Signed (Using DSC) & uploaded on the AICTE Portal. In case of any false information, AICTE shall invoke the provisions, civil and/or criminal, as per the Regulations in place.")
        return []
    
class Actiondocumentssubmissionscrutiny(Action):
    def name(self) -> Text:
        return "utter_documents_submission_scrutiny"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("A printout of the complete online application (for categories falling under Chapter I of the Approval Process Handbook), as submitted on the AICTE Web-Portal, along with the proof of payment and documents mentioned as per Annexure-1 of the Approval Process Handbook, duly attested by the Chairman/Secretary of the Trust, shall be submitted on the date of Scrutiny and uploaded on the AICTE Web-portal with a digital signature (in case of online). Failing which, the Scrutiny shall not be conducted.")
        return []
    
class Actiondocumentsubmissionprocesschapteriiiii(Action):
    def name(self) -> Text:
        return "utter_document_submission_process_chapter_ii_iii"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("For applications submitted for the categories mentioned under Chapter II and III, the documents should be submitted/uploaded as applicable in Annexure-2 of the Approval Process Handbook.")
        return []
    
class Actionpromotertrustsocietycompanyuniversityrequirements(Action):
    def name(self) -> Text:
        return "utter_promoter_trust_society_company_university_requirements"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The Promoter Trust/Society/Company shall have the built-up area as required and have its lawful possession with clear title in the name of the Promoter Trust/Society/Company/Institution or on long-term lease on or before the date of submission of the application. Additionally, the Promoter Trust/Society/Company of the proposed University can mortgage the land after the issue of the Letter of Approval (LoA), with prior intimation to AICTE, for raising resources for the development of the University situated on that land.")
        return []
    
class Actionuniversityapprovalprocesshandbooknorms(Action):
    def name(self) -> Text:
        return "utter_university_approval_process_handbook_norms"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The University shall fulfill all the norms as specified in the Approval Process Handbook. Institutions Deemed to be Universities shall also have to fulfill the norms as per UGC Regulations and statutory bodies concerned.")
        return []

class Actioncompletionofbuildingsrequirements(Action):
    def name(self) -> Text:
        return "utter_completion_of_buildings_requirements"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Buildings for the First Year of the Programme(s) should be completed in all respects as per the Infrastructure requirements specified in the Approval Process Handbook. The building plan for the entire duration of the Programme(s) of the University shall be prepared by an architect registered with the Council of Architecture/Licensed Surveyor and approved by the Competent Authority designated by the concerned State Government/UT.")
        return []
    
class ActionHeadOfUniversityQualifications(Action):
    def name(self) -> Text:
        return "utter_head_of_university_qualifications"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The Head of the University shall be named as the 'Vice Chancellor' and should have qualifications as per UGC norms.")
        return []

class Actionrestrictionsonuniversitynames(Action):
    def name(self) -> Text:
        return "utter_restrictions_on_university_names"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Yes, the Applicant shall not use the name of the University in such a way that the abbreviated form of the name becomes IIM/IIT/IISc/NIT/IISER/IIIT/IIEST/AICTE/UGC/MoE/GoI. The Applicant shall also not use specific words such as Government, India, Indian, National, All India, All India Council, Commission anywhere in the name of the University, as prohibited under the Emblems and Names (Prevention of Improper Use) Act, 1950. These restrictions do not apply if the University is established by the Government of India or its name is approved by the Government of India.")
        return []
    
class ActionapprovaloftechnicalprogramsbyUGC(Action):
    def name(self) -> Text:
        return "utter_approval_of_technical_programs_by_ugc"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The Applicant shall apply on the AICTE Web-Portal for all the Technical Programme(s) as approved by UGC for Approval.")
        return []

class Actionapplicationprocessinghandbook(Action):
    def name(self) -> Text:
        return "utter_application_processing_handbook"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The application shall be processed as per Clause 4.6 and 4.7 of the Approval Process Handbook through the Scrutiny/Re-Scrutiny Committee.")
        return []

class ActionKeyEvaluationCriteriaUGCRegulations(Action):
    def name(self) -> Text:
        return "utter_key_evaluation_criteria_ugc_regulations"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The evaluation criteria for universities and institutions Deemed to be Universities are:\n"
                                  "a. NAAC Certificate indicating score letter issued by UGC declaring the status of the University and other (if applicable).\n"
                                  "b. Notification issued by the Government under Central/State Act declaring an institution as a Central/State/Private University or Section 3 of UGC Act declaring an Institution as a Deemed to be University.\n"
                                  "c. UGC approval letter(s) for the main Campus and Off Campuses if any.\n"
                                  "d. Affidavit 2 and 5 (Universities shall have to adhere to norms and standards specified by AICTE from time to time).\n")
        return []

class Actionconsequencesofmissingdocumentsevaluation(Action):
    def name(self) -> Text:
        return "utter_consequences_of_missing_documents_evaluation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("If the specified documents are not uploaded on the portal during the evaluation process, the University may be directed to upload the same within the stipulated time. The formation of the Scrutiny/Re-Scrutiny committee and verification of the documents will be conducted online.")
        return []

class Actionevaluationofuniversitiesrunningtechnicalprograms(Action):
    def name(self) -> Text:
        return "utter_evaluation_of_universities_running_technical_programs"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Universities running technical programs for the first time are evaluated as per the requirements outlined in Chapter-I (Grant of Approval for New Institution).")
        return []

class ActionAICTEapproveduniversitiescategoriesapplication(Action):
    def name(self) -> Text:
        return "utter_aicte_approved_universities_categories_application"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Universities running AICTE approved technical programs and desiring to apply for various categories in accordance with Chapter-II (Grant of Extension of Approval for Existing Institutions) are processed as per the applicable classes defined in Chapter-II of the Approval Process Handbook.")
        return []
    
class Actionconsiderationsformedicaluniversitiesapproval(Action):
    def name(self) -> Text:
        return "utter_considerations_for_medical_universities_approval"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("For universities applying for approval in other domains, such as a Medical University, applying for approval of Engineering and Technology Programs shall be processed similarly to a new Technical Institution, provided that the university is already running courses in Engineering and Technology.")
        return []

class Actionoffcampusesconstituentcollegesrequirement(Action):
    def name(self) -> Text:
        return "utter_off_campuses_constituent_colleges_requirement"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("To consider the Off Campuses/Constituent Colleges, UGC Letter as well as NAAC mentioning to that effect shall be produced. Otherwise, the applications shall be processed as per Chapter-I (Grant of Approval for New Institution) of the Approval Process Handbook.")
        return []

class Actiondocumentsuploaddigitalsignificancesignificance(Action):
    def name(self) -> Text:
        return "utter_documents_upload_digital_signatures_significance"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Applicants shall upload all self-attested copies as per Annexure-1 (as applicable) of the Approval Process Handbook and UGC approval Letter(s) for the Main Campus and Off Campuses, if any. Applicants shall adhere to the Scrutiny/Re-Scrutiny schedule and not remain absent at the time of Scrutiny/Re-Scrutiny.")
        return []

class Actionexpertvisitcommitteenewinstitutiondeemeduniversity(Action):
    def name(self) -> Text:
        return "utter_expert_visit_committee_new_institution_deemed_university"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("An Expert Visit Committee may be conducted any time before the first batch of students has passed out to verify the fulfillment of the norms as specified in the Approval Process Handbook.")
        return []

class Actionrejectedapplicationappealprovision(Action):
    def name(self) -> Text:
        return "utter_rejected_application_appeal_provision"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("If the application for a new Institution Deemed to be University/University is rejected at the Level of Scrutiny/Re-Scrutiny, and the appeal provision is not availed, the TER Charges, after a deduction of Rs. 0.60 Lakh, shall be refunded to the Applicant.")
        return []

class Actionconditionalapprovalgrantcircumstances(Action):
    def name(self) -> Text:
        return "utter_conditional_approval_grant_circumstances"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The Council shall normally not grant Conditional Approval to any University.")
        return []

class Actionappealprocessagainstexecutivecommitteedecision(Action):
    def name(self) -> Text:
        return "utter_appeal_process_against_executive_committee_decision"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The University/Applicant, if aggrieved by the decision of the Executive Committee, shall appeal as per Clause 1.11 of the Approval Process Handbook, and the final decision of the Council shall be uploaded as per the Academic Calendar.")
        return []

class Actioninfrastructurefacultyrequirementshandbook(Action):
    def name(self) -> Text:
        return "utter_infrastructure_faculty_requirements_handbook"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Infrastructure, faculty, and other facilities shall be made available as per the norms, standards, and conditions prescribed by the Council from time to time.")
        return []

class Actionfinalapprovalrejectioncommunication(Action):
    def name(self) -> Text:
        return "utter_final_approval_rejection_communication"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("A final Letter of Approval/ Letter of Rejection with the reasons for rejection of the application shall be issued to the University through the Web-Portal as per the Academic Calendar.")
        return []
    
class Actiondeadlineforapprovalletterissuance(Action):
    def name(self) -> Text:
        return "utter_deadline_for_approval_letter_issuance"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("LoA shall not be granted after the last date as mentioned in the Academic Calendar.")
        return []

class Actionsecuritydepositexemptedinstitutions(Action):
    def name(self) -> Text:
        return "utter_security_deposit_exempted_institutions"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Central University/ State University/ Institution Deemed to be University (Government) are not required to pay the Security Deposit.")
        return []
    
class Actionprivateuniversitiessecuritydepositexemption(Action):
    def name(self) -> Text:
        return "utter_private_universities_security_deposit_exemption"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Private Universities/Institution Deemed to be University (Private) which were in existence for more than 10 years with UGC are EXEMPTED from the payment of Security Deposit, else the University shall pay the Security Deposit for 10 Years as per Chapter-I (Table 1.4) of this Approval Process Handbook.")
        return []

class ActionSecurityDepositCreationForNewProgrammeLevel(Action):
    def name(self) -> Text:
        return "utter_security_deposit_creation_for_new_programme_level"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("If any University is starting a new Programme/Level, it shall create the Security Deposit as per the requirements of the Approval Process Handbook, even if the University is in existence for more than 10 years with UGC.\n"
                                  "NOTE:\n"
                                  "I. Universities which were granted approval from AICTE earlier as a Technical Institution and created Security Deposit and got released after the maturity period are not required to pay the Security Deposit; else the University shall pay the Security Deposit for the remaining period of 10 years, as applicable.\n"
                                  "II. What happens to the amount deposited by the University?\n"
                                  "AII: The amount deposited by the University shall remain with the Council. The interest accrued on this deposit shall be utilized by the Council for Institutional Development activities, Quality Improvement Programme for Faculty members, and giving Scholarships to students.\n"
                                  "III. What is the condition for returning the deposited amount to the Trust/Society/Company?\n"
                                  "AIII: The Principal amount ONLY shall be returned to the Trust/Society/Company on completion of the term. However, the term of the deposited amount can be extended for a further period as shall be decided on a case-to-case basis and/or forfeited in case of any violation of norms, conditions, and requirements and/or Non-Performance by the University and/or Complaints against the University.\n")
        return []

class Actionexpertvisitcommitteeexemptionsupernumeraryseats(Action):
    def name(self) -> Text:
        return "utter_expert_visit_committee_exemption_supernumerary_seats"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Expert Visit Committee for the Introduction of supernumerary seats for OCI/Foreign Nationals/Children of Indian Workers in the Gulf Countries shall be exempted from the requirements and eligibility mentioned in the concerned Clauses of the Approval Process Handbook for universities eligible for Graded Autonomy.")
        return []
    
class ActionTERChargesApplicableApprovalHandbook(Action):
    def name(self) -> Text:
        return "utter_ter_charges_applicable_approval_handbook"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Technical Education Regulatory (TER) Charges as mentioned in the Approval Process Handbook are applicable for universities.\n"
                                  "NOTE: In an extraordinary circumstance, if an additional Scrutiny Committee, Expert Visit Committee, and Standing Hearing Committee/Standing Appellate Committee has to be conducted (inclusive of the Court directions to any type of institutions), then the Applicant has to remit an additional TER Charges as applicable in Clause 4.5.2.\n")
        return []

class Actionextensionofapprovalprocessingratification(Action):
    def name(self) -> Text:
        return "utter_extension_of_approval_processing_ratification"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("The applications for Extension of Approval are processed as per the procedure specified in the Approval Process Handbook, and the Executive Committee/Council shall grant Extension of Approval as applicable for the universities to continue for the conduct of Technical Programme(s) and Course(s). The decisions taken by the Executive Committee shall be ratified by the Council.")
        return []

class Actiongradedautonomyeligibleuniversitiesintakeincrease(Action):
    def name(self) -> Text:
        return "utter_graded_autonomy_eligible_universities_intake_increase"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Universities eligible for Graded Autonomy need to submit an application to the Council indicating the increase in Intake in the Courses/New Course(s) in Emerging/Multidisciplinary areas. The Council shall grant approval to those Programmes/Courses. However, such universities shall have to update the data in AICTE Web-Portal on an annual basis and comply with the norms and standards as specified by AICTE from time to time.")
        return []

class Actionactionsincomplaintsnormsviolation(Action):
    def name(self) -> Text:
        return "utter_actions_in_complaints_norms_violation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("If any complaints are received about the violation of the norms, AICTE shall inspect the university and inform UGC to take appropriate action. In the case of an Institution Deemed to be University, the action, as specified in the Approval Process Handbook, shall be initiated and informed to UGC & MoE (as applicable).")
        return []
    
class Actionconditionsnotgrantingextensionofapproval(Action):
    def name(self) -> Text:
        return "utter_conditions_not_granting_extension_of_approval"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Extension of Approval shall not be granted after the last date as mentioned in the Academic Calendar.")
        return []
    
class Actionobtainingextensionofapprovalletter(Action):
    def name(self) -> Text:
        return "utter_obtaining_extension_of_approval_letter"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Institutional information shall be updated on the AICTE Web-Portal by the institution, and the Extension of Approval letter can be downloaded from there.")
        return []
    
class Actionadmissioneligibilitycriteria(Action):
    def name(self) -> Text:
        return "utter_admission_eligibility_criteria"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Students' eligibility for admission shall be as per Annexure-8 of the Approval Process Handbook.")
        return []
    
class Actionacademiccalendarrequirementuniversities(Action):
    def name(self) -> Text:
        return "utter_academic_calendar_requirement_universities"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(" All universities shall follow the Academic Calendar as notified by the Council from time to time.")
        return []

class Actionstudentenrollmentdetailsuploaddeadline(Action):
    def name(self) -> Text:
        return "utter_student_enrollment_details_upload_deadline"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Student enrollment details shall be uploaded on the AICTE Web-Portal before the last date (Academic Calendar for the respective year).")
        return []
    
class Actiongoverningbodiesconstitutionprivatestateprivateuniversity(Action):
    def name(self) -> Text:
        return "utter_governing_bodies_constitution_private_state_private_university"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Board of Governors (BoG)/Board of Management (BoM) shall be constituted for the Institution Deemed to be University (Private)/State Private University. BoM of universities shall be as per the Acts and Statutes of UGC. The minutes of the meetings shall be uploaded periodically on the website of the universities.")
        return []

class Actionmeasuresmaintaininghighstandardtechnicaleducation(Action):
    def name(self) -> Text:
        return "utter_measures_maintaining_high_standard_technical_education"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("To maintain a high standard in Technical Education, universities shall adopt quality measures such as the revision of curriculum in tune with the changing trends in industrial development, performing Academic Audit, conducting innovative academic and sponsored research, publishing papers in refereed journals, and applying for granting Patents.")
        return []
    
class Actionuniversitiesexemptedannualapprovaltechnicalprograms(Action):
    def name(self) -> Text:
        return "utter_universities_exempted_annual_approval_technical_programs"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Institutions Deemed to be Universities that have been recognized as an Institute of Eminence (IOE) by the Ministry of Education, Government of India shall be exempted from going through the process of approval annually for offering Technical Programmes/Courses. However, such universities shall have to update the data on the AICTE Web-Portal on an annual basis and comply with the norms and standards as specified by AICTE from time to time.")
        return []

class Actionactionsunapprovedtechnicalprogramrunning(Action):
    def name(self) -> Text:
        return "utter_actions_unapproved_technical_program_running"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("An Institution (Deemed to be University) found running a technical programme without prior approval of the council shall be liable for appropriate penal action as per Chapter VII.")
        return []

class Actionscrutinyrescrutinyconductingprocess(Action):
    def name(self) -> Text:
        return "utter_scrutiny_re_scrutiny_conducting_process"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("All the Scrutiny/Re-Scrutiny shall be conducted preferably in online mode. Under extraordinary circumstances (including Court directions), the Scrutiny/Re-Scrutiny shall be conducted in offline mode also. Proceedings of the Scrutiny/Re-Scrutiny shall be recorded to have Transparency and Accountability. The signature of experts on documents submitted/uploaded by the Institute on the portal is not necessary if verified online.")
        return []
