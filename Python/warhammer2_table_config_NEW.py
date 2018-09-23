# UPDATED AT: 2018-09-22 11:46:55.517000
keyDict = {
"abilities_tables": ['ability'], 
"achievements_tables": ['key'], 
"action_results_additional_outcomes_tables": ['key'], 
"action_results_tables": ['key'], 
"advice_info_texts_tables": ['key'], 
"advice_levels_info_text_juncs_tables": ['advice_info_text', 'advice_level'], # has no unique columns, will check column groups instead
"advice_levels_tables": ['key'], 
"advice_threads_tables": ['thread'], 
"advisors_tables": ['advisor_name', 'advisor_icon_path'], # Too many unique columns, will use them all
"agents_tables": ['key'], 
"agent_ability_categories_tables": ['key'], 
"agent_actions_tables": ['unique_id'], 
"agent_attributes_tables": ['key'], 
"agent_culture_details_tables": [None], # NO TSV FILES FOUND IN FOLDER
"agent_localisations_tables": ['key'], 
"agent_subtypes_tables": ['key'], 
"agent_subtype_subculture_overrides_tables": ['subtype', 'agent', 'icon'], # Too many unique columns, will use them all
"agent_to_agent_abilities_tables": ['agent'], 
"agent_to_agent_attributes_tables": ['attribute', 'agent'], # has no unique columns, will check column groups instead
"agent_uniforms_tables": ['uniform_name'], 
"aide_de_camp_speeches_tables": ['key'], 
"ai_usage_groups_tables": ['unknown0'], 
"ancillaries_categories_faction_junctions_tables": ['ancillary_category', 'faction'], # has no unique columns, will check column groups instead
"ancillaries_categories_tables": ['category', 'sort_order'], # Too many unique columns, will use them all
"ancillaries_included_agent_subtypes_tables": ['agent_subtype', 'ancillary'], # has no unique columns, will check column groups instead
"ancillaries_required_skills_tables": ['ancillary'], 
"ancillaries_subcategories_tables": ['subcategory'], 
"ancillaries_tables": ['key'], 
"ancillary_included_subcultures_tables": ['ancillary', 'subculture'], # has no unique columns, will check column groups instead
"ancillary_info_tables": ['ancillary'], 
"ancillary_salvage_resources_tables": ['category', 'min_uniqueness_score', 'category', 'salvage_resources'], # has no unique columns, will check column groups instead
"ancillary_to_effects_tables": ['ancillary', 'effect'], # has no unique columns, will check column groups instead
"ancillary_to_included_agents_tables": ['ancillary', 'agent'], # has no unique columns, will check column groups instead
"ancillary_types_tables": ['type'], 
"ancillary_uniqueness_groupings_tables": ['group_key'], 
"animation_set_prebattle_groups_tables": ['key'], 
"animation_set_prebattle_group_junctions_tables": ['anim_set'], 
"animation_set_prebattle_group_view_configurations_tables": ['attacker', 'defender'], # has no unique columns, will check column groups instead
"area_of_effect_displays_tables": ['unknown1'], 
"armed_citizenry_units_to_unit_groups_junctions_tables": ['id'], 
"armed_citizenry_unit_groups_tables": ['unit_group'], 
"army_special_abilities_for_faction_junctions_tables": ['army_special_ability', 'faction'], # has no unique columns, will check column groups instead
"army_special_abilities_tables": ['unknown0', 'unknown1', 'unknown2'], # Too many unique columns, will use them all
"audio_abilities_tables": ['unknown0'], 
"audio_ability_phases_tables": ['key'], 
"audio_armour_types_tables": ['key'], 
"audio_battle_environments_tables": ['name'], 
"audio_battle_environment_loops_tables": ['event_start', 'event_stop', 'name'], # Too many unique columns, will use them all
"audio_battle_environment_loop_junctions_tables": ['environment', 'loop'], # has no unique columns, will check column groups instead
"audio_battle_environment_one_shots_tables": ['name'], 
"audio_battle_environment_one_shot_junctions_tables": [None], # has no unique columns or column groups!
"audio_battle_environment_reverbs_tables": ['aux_fl', 'aux_fr', 'aux_rl', 'aux_rr', 'name'], # Too many unique columns, will use them all
"audio_battle_environment_reverb_junctions_tables": ['environment', 'reverb', 'environment', 'type'], # has no unique columns, will check column groups instead
"audio_battle_environment_weathers_tables": ['name', 'wind_intensity_modifier'], # Too many unique columns, will use them all
"audio_battle_environment_weather_loop_junctions_tables": ['loop'], 
"audio_battle_environment_weather_one_shot_junctions_tables": ['one_shot', 'weather'], # Too many unique columns, will use them all
"audio_battle_ground_types_tables": ['key'], 
"audio_campaign_buildings_tables": ['key'], 
"audio_campaign_building_enums_tables": ['key'], 
"audio_campaign_environment_ground_type_sounds_tables": ['key'], 
"audio_campaign_environment_ground_type_sound_assignments_tables": ['map', 'sound'], # has no unique columns, will check column groups instead
"audio_campaign_environment_ground_type_sound_ground_types_tables": ['ground_type'], 
"audio_campaign_environment_ground_type_sound_sounds_tables": ['looping_sound', 'sound'], # Too many unique columns, will use them all
"audio_campaign_environment_looping_sounds_tables": ['key'], 
"audio_campaign_environment_static_sounds_tables": ['looping_sound', 'map'], # has no unique columns, will check column groups instead
"audio_campaign_environment_tree_sounds_tables": ['key'], 
"audio_campaign_environment_tree_sound_assignments_tables": ['map', 'sound'], # has no unique columns, will check column groups instead
"audio_campaign_environment_tree_sound_sounds_tables": ['looping_sound', 'tree_sound'], # Too many unique columns, will use them all
"audio_campaign_environment_tree_sound_trees_tables": ['sound', 'tree'], # Too many unique columns, will use them all
"audio_campaign_maps_tables": ['key'], 
"audio_campaign_stances_tables": ['stance'], 
"audio_entity_actors_tables": ['key'], 
"audio_entity_looping_sounds_tables": ['key'], 
"audio_entity_random_vocalisations_tables": ['key'], 
"audio_entity_types_tables": ['unknown5'], 
"audio_entity_type_limitations_tables": ['key'], 
"audio_explosions_tables": [None], # NO TSV FILES FOUND IN FOLDER
"audio_group_sounds_tables": ['name'], 
"audio_group_sound_assignments_tables": ['entity_type', 'situation'], # has no unique columns, will check column groups instead
"audio_group_sound_groupings_tables": ['key'], 
"audio_markers_tables": ['key'], 
"audio_materials_tables": ['key'], 
"audio_melee_hit_types_tables": ['key'], 
"audio_melee_weapon_types_tables": ['key'], 
"audio_metadata_tags_tables": ['key'], 
"audio_metadata_tag_entity_overrides_tables": ['unknown0', 'unknown1'], # has no unique columns, will check column groups instead
"audio_missile_weapon_types_tables": ['key'], 
"audio_projectiles_tables": ['key'], 
"audio_projectile_bombardments_tables": ['key'], 
"audio_projectile_limitations_tables": ['unknown0', 'unknown6'], # Too many unique columns, will use them all
"audio_shield_types_tables": ['key'], 
"audio_sphere_of_influences_tables": ['unknown2'], 
"audio_sphere_of_influence_groups_tables": ['unknown0'], 
"audio_sphere_of_influence_one_shots_tables": ['unknown0', 'unknown3'], # Too many unique columns, will use them all
"audio_technologies_tables": ['unknown0', 'unknown1'], # Too many unique columns, will use them all
"audio_ui_categories_tables": ['unknown0'], 
"audio_vo_actor_groups_tables": ['name'], 
"autoresolver_ai_usage_group_combat_potential_modifiers_tables": ['usage_group'], 
"autoresolver_battle_types_tables": ['unknown4'], 
"autoresolver_modifier_group_keys_tables": ['key'], 
"autoresolver_modifier_group_lookups_tables": ['unknown1'], 
"autoresolver_modifier_group_to_modifiers_tables": ['unknown1'], 
"autoresolver_modifier_targets_tables": ['unknown0'], 
"autoresolver_player_types_tables": ['unknown4'], 
"banners_permitted_unit_sets_tables": ['banner', 'unit_set'], # has no unique columns, will check column groups instead
"banners_tables": ['banner', 'effect_bundle'], # Too many unique columns, will use them all
"battlefield_buildings_names_tables": ['key'], 
"battlefield_buildings_tables": ['key'], 
"battlefield_buildings_with_projectiles_names_tables": ['projectile'], 
"battlefield_building_categories_tables": ['category'], 
"battlefield_deployable_siege_items_tables": ['key'], 
"battlefield_engines_tables": ['key'], 
"battlefield_siege_vehicles_custom_battles_tables": ['vehicle'], 
"battlefield_siege_vehicles_tables": ['key'], 
"battles_tables": ['key'], 
"battle_ai_abilities_usage_params_tables": ['usage_param'], 
"battle_ai_abilities_usage_templates_to_params_tables": ['parameter', 'template'], # has no unique columns, will check column groups instead
"battle_ai_abilities_usage_template_names_tables": ['ai_ability_usage_template_key'], 
"battle_animations_table_tables": ['key'], 
"battle_cameras_tables": ['key'], 
"battle_camera_shake_parameters_tables": ['key'], 
"battle_catchment_override_areas_tables": ['area'], 
"battle_catchment_override_battle_mappings_tables": [None], # has no unique columns or column groups!
"battle_catchment_override_groups_tables": ['group'], 
"battle_catchment_override_group_battles_tables": ['battle_map_location', 'group'], # has no unique columns, will check column groups instead
"battle_cinematic_event_categories_tables": ['key'], 
"battle_climate_weather_descriptions_tables": ['key'], 
"battle_context_army_special_ability_junctions_tables": ['unknown0', 'unknown1', 'unknown2'], # Too many unique columns, will use them all
"battle_context_unit_attribute_junctions_tables": ['battle_context'], # 'key' column is not unique
"battle_entities_gradient_strategy_enums_tables": ['key'], 
"battle_entities_size_enums_tables": ['key'], 
"battle_entities_tables": ['key'], 
"battle_entity_effects_junctions_tables": ['key'], 
"battle_entity_effects_tables": ['name'], 
"battle_entity_stats_tables": ['key'], 
"battle_misc_effects_tables": ['name'], 
"battle_personalities_tables": ['key'], 
"battle_result_types_tables": ['battle_result_type', 'unit_exp_gain'], # Too many unique columns, will use them all
"battle_set_pieces_tables": ['unknown3'], 
"battle_set_piece_armies_characters_items_tables": ['character_item', 'character_name'], # has no unique columns, will check column groups instead
"battle_set_piece_armies_characters_junctions_tables": ['army_name', 'character_name'], # has no unique columns, will check column groups instead
"battle_set_piece_armies_characters_skillsets_skills_tables": ['skillset_key', 'sort_order'], # has no unique columns, will check column groups instead
"battle_set_piece_armies_characters_skillsets_tables": ['key'], 
"battle_set_piece_armies_characters_skills_tables": ['character_name', 'skill'], # has no unique columns, will check column groups instead
"battle_set_piece_armies_characters_tables": ['character_name'], 
"battle_set_piece_armies_effect_bundles_tables": ['unknown0', 'unknown1'], # has no unique columns, will check column groups instead
"battle_set_piece_armies_junctions_tables": ['army_name', 'battle_name'], # has no unique columns, will check column groups instead
"battle_set_piece_armies_tables": ['unknown4'], 
"battle_set_piece_armies_units_junctions_tables": [None], # has no unique columns or column groups!
"battle_set_piece_armies_units_tables": ['unit_name'], 
"battle_set_piece_campaign_battle_scenes_tables": ['unknown0'], 
"battle_set_piece_campaign_battle_scene_view_configurations_tables": ['unknown4'], 
"battle_set_piece_frontend_groups_tables": ['unknown0', 'unknown1'], # Too many unique columns, will use them all
"battle_set_piece_frontend_groups_to_characters_tables": ['character'], 
"battle_siege_vehicle_permissions_tables": ['faction', 'vehicle'], # has no unique columns, will check column groups instead
"battle_skeletons_tables": ['name'], 
"battle_types_tables": ['type'], 
"battle_types_to_victory_conditions_tables": ['battle_type', 'attacker_victory_condition'], # has no unique columns, will check column groups instead
"battle_type_setup_limits_tables": ['id'], 
"battle_vortexs_tables": ['vortex_key'], 
"battle_vortex_collision_responses_tables": ['description', 'vortex_collision_type'], # Too many unique columns, will use them all
"battle_vortex_launch_sources_tables": ['description', 'suggested_launch_source'], # Too many unique columns, will use them all
"battle_weather_types_tables": ['key'], 
"bmd_export_types_tables": ['description', 'name'], # Too many unique columns, will use them all
"bmd_layer_groups_tables": ['key'], 
"building_chains_tables": ['key'], 
"building_chain_availabilities_tables": ['key'], 
"building_chain_availability_sets_tables": ['building_chain', 'id'], # has no unique columns, will check column groups instead
"building_chain_availability_set_ids_tables": ['key'], 
"building_culture_variants_tables": [None], # has no unique columns or column groups!
"building_downgrade_junctions_tables": ['from'], 
"building_effects_junction_tables": ['building', 'effect'], # has no unique columns, will check column groups instead
"building_instances_tables": ['key'], 
"building_levels_campaign_bmd_layer_group_junctions_tables": ['building_level', 'campaign_bmd_layer_group'], # has no unique columns, will check column groups instead
"building_levels_tables": ['level_name'], # 'key' column is not unique
"building_level_armed_citizenry_junctions_tables": ['id'], 
"building_level_required_buildings_tables": ['building_level', 'required'], # Too many unique columns, will use them all
"building_sets_tables": ['key'], 
"building_set_to_building_junctions_tables": [None], # has no unique columns or column groups!
"building_states_tables": ['key'], 
"building_superchains_tables": ['key'], 
"building_units_allowed_tables": ['key'], 
"building_upgrades_junction_tables": ['from', 'to'], # has no unique columns, will check column groups instead
"cai_agent_distribution_profiles_tables": ['key'], 
"cai_agent_distribution_types_tables": ['key'], 
"cai_agent_embed_profiles_tables": ['key'], 
"cai_agent_embed_profile_agent_type_junctions_tables": ['agent_embed_profile_key', 'agent_type_key', 'free_agent_type_cap', 'free_agent_type_cap_per_horde_multiplier', 'free_agent_type_cap_per_region_multiplier', 'unknown5'], # Too many unique columns, will use them all
"cai_agent_record_to_cai_agent_type_junctions_tables": ['agent_record_key', 'unknown2', 'agent_type_key', 'unknown2'], # has no unique columns, will check column groups instead
"cai_agent_recruitment_profiles_tables": ['key'], 
"cai_agent_recruitment_types_tables": ['key'], 
"cai_agent_types_tables": ['key'], 
"cai_agent_type_distribution_profile_junctions_tables": ['agent_type_key'], 
"cai_agent_type_recruitment_profile_junctions_tables": ['agent_type_key'], 
"cai_character_skill_synergies_tables": ['unknown1'], 
"cai_character_skill_synergy_levels_tables": ['unknown0', 'unknown1'], # Too many unique columns, will use them all
"cai_construction_system_blocking_buildings_tables": ['building_end', 'building_start', 'category'], # Too many unique columns, will use them all
"cai_construction_system_blocking_categories_tables": ['key'], 
"cai_construction_system_building_values_tables": ['building_or_building_range_start_inclusive', 'cai_construction_system_category_group', 'building_range_end_inclusive', 'cai_construction_system_category_group'], # has no unique columns, will check column groups instead
"cai_construction_system_categories_tables": ['key'], 
"cai_construction_system_category_groups_tables": ['key'], 
"cai_construction_system_province_template_assignment_policies_tables": ['key'], 
"cai_construction_system_strategic_context_template_policies_tables": ['key'], 
"cai_construction_system_strategic_context_template_policy_junctions_tables": ['cai_construction_system_strategic_context_policy', 'cai_strategic_context', 'cai_construction_system_template', 'cai_strategic_context'], # has no unique columns, will check column groups instead
"cai_construction_system_superchain_hints_tables": ['super_chain_key'], 
"cai_construction_system_synergies_tables": ['unknown2', 'potential_buiding_chain_key', 'unknown2', 'unknown4', 'unknown2', 'unknown5'], # has no unique columns, will check column groups instead
"cai_construction_system_synergy_levels_tables": ['key'], 
"cai_construction_system_synergy_policies_tables": ['key'], 
"cai_construction_system_synergy_scopes_tables": ['key'], 
"cai_construction_system_templates_junctions_tables": ['cai_construction_system_category_group', 'cai_construction_system_template'], # has no unique columns, will check column groups instead
"cai_construction_system_templates_tables": ['key'], 
"cai_construction_system_template_assignment_schemes_tables": ['scheme_key'], 
"cai_construction_system_unblocking_buildings_tables": ['building_end', 'building_start'], # Too many unique columns, will use them all
"cai_diplomacy_complex_treacheries_tables": ['first_event'], 
"cai_diplomacy_excluded_factions_tables": [None], # NO TSV FILES FOUND IN FOLDER
"cai_diplomacy_simple_treacheries_tables": ['event'], 
"cai_factions_to_hint_profile_groups_tables": ['unknown0', 'unknown2'], # has no unique columns, will check column groups instead
"cai_faction_statuses_tables": ['faction_status'], 
"cai_hint_profile_groups_tables": ['unknown0', 'unknown1'], # Too many unique columns, will use them all
"cai_military_aggressiveness_policies_tables": ['key'], 
"cai_military_behaviour_policies_tables": ['key'], 
"cai_personalities_budget_allocations_tables": ['key'], 
"cai_personalities_budget_allocation_policy_junctions_tables": ['budget_context_key', 'budget_policy_key'], # has no unique columns, will check column groups instead
"cai_personalities_budget_policies_tables": ['key'], 
"cai_personalities_character_skill_selection_policies_skill_utilization_hints_junctions_tables": ['skill_utilization_hint_key'], 
"cai_personalities_character_skill_selection_policies_tables": ['key'], 
"cai_personalities_construction_preference_policies_tables": ['key'], 
"cai_personalities_construction_system_policies_tables": ['key'], 
"cai_personalities_income_allocations_tables": ['key'], 
"cai_personalities_income_allocation_policies_tables": ['key'], 
"cai_personalities_income_allocation_policy_strategic_context_junctions_tables": ['income_allocation_policy_key', 'strategic_context_key'], # has no unique columns, will check column groups instead
"cai_personalities_reliability_policies_tables": ['key'], 
"cai_personalities_religion_change_management_policies_tables": ['key'], 
"cai_personalities_religious_conversion_policies_tables": ['key'], 
"cai_personalities_tables": ['unknown3'], 
"cai_personalities_task_management_system_task_generator_profiles_tables": ['key'], 
"cai_personalities_technology_researches_tables": ['key'], 
"cai_personalities_technology_research_path_junctions_tables": ['key', 'path_key'], # has no unique columns, will check column groups instead
"cai_personalities_technology_research_policies_tables": ['key'], 
"cai_personalities_technology_research_policy_strategic_context_junctions_tables": [None], # has no unique columns or column groups!
"cai_personalities_tms_task_generator_profile_faction_statuses_junctions_tables": ['cai_action_status_key', 'task_generator_policy_key'], # has no unique columns, will check column groups instead
"cai_personality_cultural_components_tables": ['id'], 
"cai_personality_cultural_relations_overrides_tables": [None], # has no unique columns or column groups!
"cai_personality_deal_evaluation_components_tables": ['id'], 
"cai_personality_deal_evaluation_component_overrides_tables": ['component'], 
"cai_personality_deal_evaluation_deal_component_names_tables": ['id'], 
"cai_personality_deal_evaluation_deal_component_values_tables": ['deal_component', 'personality_component'], # has no unique columns, will check column groups instead
"cai_personality_deal_generation_components_tables": ['id'], 
"cai_personality_deal_generation_component_overrides_tables": ['component'], 
"cai_personality_deal_generation_generators_tables": ['id'], 
"cai_personality_deal_generation_generator_priorities_tables": ['component_key', 'generator_key'], # has no unique columns, will check column groups instead
"cai_personality_diplomatic_components_tables": ['id'], 
"cai_personality_diplomatic_component_overrides_tables": ['component'], 
"cai_personality_diplomatic_events_tables": ['id'], 
"cai_personality_diplomatic_event_values_tables": ['component_id', 'event_id'], # has no unique columns, will check column groups instead
"cai_personality_diplomatic_treaty_types_tables": ['key'], 
"cai_personality_diplomatic_treaty_values_tables": ['component_id', 'treaty'], # has no unique columns, will check column groups instead
"cai_personality_empire_rivalry_components_tables": ['key'], 
"cai_personality_groups_tables": ['key'], 
"cai_personality_group_junctions_tables": ['group_key', 'personality_key'], # has no unique columns, will check column groups instead
"cai_personality_group_overrides_tables": [None], # has no unique columns or column groups!
"cai_personality_negotiation_components_tables": ['id', 'no_offer_chance'], # Too many unique columns, will use them all
"cai_personality_occupation_decision_components_tables": ['unknown0'], 
"cai_personality_occupation_decision_policies_tables": ['unknown2'], 
"cai_personality_occupation_decision_priorities_tables": ['unknown2', 'unknown0'], # has no unique columns, will check column groups instead
"cai_personality_religious_components_tables": ['id', 'short_description', 'long_description'], # Too many unique columns, will use them all
"cai_personality_strategic_components_tables": ['id'], 
"cai_personality_strategic_desired_attitudes_tables": ['strategic_component'], 
"cai_personality_strategic_resource_values_tables": ['resource', 'strategic_component'], # has no unique columns, will check column groups instead
"cai_personality_trespassing_components_tables": ['key'], 
"cai_region_groups_tables": ['unknown0'], 
"cai_region_groups_to_regions_junctions_tables": ['unknown0', 'unknown1'], # has no unique columns, will check column groups instead
"cai_region_hints_tables": ['key'], 
"cai_region_hint_groups_tables": ['unknown0', 'unknown1'], # Too many unique columns, will use them all
"cai_region_hint_profiles_tables": ['key'], 
"cai_region_hint_profiles_to_region_hint_groups_tables": ['unknown0', 'unknown1'], # has no unique columns, will check column groups instead
"cai_region_hint_profile_overrides_tables": ['unknown0', 'unknown1'], # Too many unique columns, will use them all
"cai_ritual_check_types_tables": ['key'], 
"cai_ritual_ritual_check_type_junctions_tables": ['unknown0'], 
"cai_ritual_variables_tables": ['unknown1'], 
"cai_ritual_weights_tables": ['unknown0'], 
"cai_siege_strength_modifiers_tables": ['assault_strength_modifier', 'defence_strength_modifier', 'subculture'], # Too many unique columns, will use them all
"cai_stance_hints_tables": ['unknown0', 'unknown1', 'unknown2'], # Too many unique columns, will use them all
"cai_strategic_context_types_tables": ['key'], 
"cai_task_management_system_task_generators_tables": ['key'], 
"cai_task_management_system_task_generator_groups_generators_junctions_tables": ['task_generator_group_key', 'task_generator_key'], # has no unique columns, will check column groups instead
"cai_task_management_system_task_generator_groups_tables": ['key'], 
"cai_task_management_system_task_generator_group_overrides_tables": ['task_generator_group'], 
"cai_variables_overides_tables": ['cai_variable_key', 'optional_difficulty_level'], # has no unique columns, will check column groups instead
"cai_variables_tables": ['key'], 
"campaigns_campaign_variables_junctions_tables": [None], # has no unique columns or column groups!
"campaign_ai_managers_tables": ['manager'], 
"campaign_ai_manager_behaviour_junctions_tables": ['manager', 'behaviour'], # has no unique columns, will check column groups instead
"campaign_ai_technology_managers_tables": ['key'], 
"campaign_ai_technology_path_junctions_tables": ['technology_key'], 
"campaign_ai_technology_research_profiles_tables": ['key'], 
"campaign_ambush_ground_types_tables": ['key'], 
"campaign_autoresolver_skirmish_effectiveness_relative_to_speeds_tables": ['proportional_effectiveness_skirmisher_to_other', 'relative_speed_skirmisher_to_other'], # Too many unique columns, will use them all
"campaign_battle_presets_tables": ['key'], 
"campaign_battle_scenes_tables": ['bmd', 'colour', 'bmd', 'culture', 'colour', 'culture'], # has no unique columns, will check column groups instead
"campaign_bmd_layer_group_bmd_export_types_junctions_tables": ['bmd_export_types', 'campaign_bmd_layer_group'], # Too many unique columns, will use them all
"campaign_bonus_value_battle_context_battle_type_junctions_tables": ['battle_context_key', 'battle_type_key'], # has no unique columns, will check column groups instead
"campaign_bonus_value_battle_context_culture_junctions_tables": ['battle_context_key', 'culture_key'], # has no unique columns, will check column groups instead
"campaign_bonus_value_battle_context_faction_junctions_tables": ['faction_key'], 
"campaign_bonus_value_battle_context_force_status_junctions_tables": ['battle_context_key', 'force_status_key'], # has no unique columns, will check column groups instead
"campaign_bonus_value_battle_context_ground_type_junctions_tables": ['battle_context_key', 'ground_type_key'], # has no unique columns, will check column groups instead
"campaign_bonus_value_battle_context_specifiers_tables": ['key'], 
"campaign_bonus_value_battle_context_territory_status_junctions_tables": ['battle_context_key', 'territory_status_key'], # has no unique columns, will check column groups instead
"campaign_building_chain_slot_unlocks_tables": ['unknown0', 'unknown1', 'unknown0', 'unknown2'], # has no unique columns, will check column groups instead
"campaign_camera_map_bounds_tables": ['campaign', 'max_x', 'max_y'], # Too many unique columns, will use them all
"campaign_character_arts_tables": ['art_set_id', 'id'], # Too many unique columns, will use them all
"campaign_character_art_sets_tables": ['art_set_id'], 
"campaign_character_uniform_ancillary_junctions_tables": ['ancillary', 'art_set'], # has no unique columns, will check column groups instead
"campaign_climate_change_phases_tables": ['campaign', 'human_imperium_threshold', 'phase', 'round_threshold'], # Too many unique columns, will use them all
"campaign_companion_army_details_tables": ['group'], 
"campaign_composite_scenes_tables": ['filename', 'id'], # Too many unique columns, will use them all
"campaign_cultural_relations_tables": [None], # has no unique columns or column groups!
"campaign_difficulty_handicap_effects_tables": [None], # has no unique columns or column groups!
"campaign_effect_scopes_tables": ['key'], 
"campaign_effect_scope_agent_junctions_tables": ['agent_key', 'campaign_effect_scope_key'], # has no unique columns, will check column groups instead
"campaign_effect_scope_categories_tables": ['key'], 
"campaign_effect_scope_character_force_relationship_junctions_tables": ['campaign_effect_scope_key', 'force_relationship_key'], # Too many unique columns, will use them all
"campaign_effect_scope_territories_tables": ['key'], 
"campaign_effect_scope_to_category_junctions_tables": ['scope', 'category'], # has no unique columns, will check column groups instead
"campaign_faction_feature_forest_overrides_tables": ['unknown1'], 
"campaign_faction_religion_effects_tables": ['effects_bundle', 'id', 'religion'], # Too many unique columns, will use them all
"campaign_features_tables": ['feature', 'group'], # has no unique columns, will check column groups instead
"campaign_ground_types_tables": ['type'], 
"campaign_groups_tables": ['id'], 
"campaign_group_abandoned_cultures_overrides_tables": ['campaign_group'], 
"campaign_group_agent_action_composite_scenes_tables": ['unknown0'], 
"campaign_group_crafting_infos_tables": ['campaign_group', 'unique_resource'], # Too many unique columns, will use them all
"campaign_group_food_effects_tables": ['key'], 
"campaign_group_food_unique_agent_charges_tables": ['campaign_group'], 
"campaign_group_loyalty_dilemmas_tables": ['unknown1'], 
"campaign_group_members_tables": ['id'], 
"campaign_group_member_criteria_action_results_tables": ['member'], 
"campaign_group_member_criteria_actor_genders_tables": ['gender', 'member'], # Too many unique columns, will use them all
"campaign_group_member_criteria_agent_subtypes_tables": ['unknown0', 'unknown1'], # Too many unique columns, will use them all
"campaign_group_member_criteria_attrition_types_tables": ['member'], 
"campaign_group_member_criteria_campaigns_tables": ['member'], 
"campaign_group_member_criteria_climates_tables": ['unknown1'], 
"campaign_group_member_criteria_cultures_tables": ['member'], 
"campaign_group_member_criteria_culture_settlement_occupation_options_tables": ['member', 'culture_settlement_occupation_option'], # Too many unique columns, will use them all
"campaign_group_member_criteria_diplomatic_attitudes_tables": ['member'], 
"campaign_group_member_criteria_factions_tables": ['member'], 
"campaign_group_member_criteria_ministerial_positions_tables": ['member'], 
"campaign_group_member_criteria_numeric_ranges_tables": ['member'], 
"campaign_group_member_criteria_originating_cultures_tables": ['member'], 
"campaign_group_member_criteria_originating_subcultures_tables": ['member'], 
"campaign_group_member_criteria_pooled_resources_tables": ['unknown0'], 
"campaign_group_member_criteria_regions_tables": ['member'], 
"campaign_group_member_criteria_region_owner_subcultures_tables": ['member'], 
"campaign_group_member_criteria_subcultures_tables": ['member'], 
"campaign_group_member_criteria_values_tables": ['member'], 
"campaign_group_morale_effects_tables": ['key'], 
"campaign_group_occupation_purchasable_primary_slot_levels_tables": ['unknown1'], 
"campaign_group_pending_battle_purchasable_effects_tables": ['unknown0', 'unknown1'], # Too many unique columns, will use them all
"campaign_group_plagues_tables": ['unknown0', 'unknown1'], # Too many unique columns, will use them all
"campaign_group_plague_military_force_effects_tables": ['unknown0', 'unknown1'], # Too many unique columns, will use them all
"campaign_group_plague_region_effects_tables": ['unknown0', 'unknown1'], # Too many unique columns, will use them all
"campaign_group_pooled_resources_tables": ['unknown0'], 
"campaign_group_pooled_resource_effects_tables": ['unknown0', 'unknown2'], # Too many unique columns, will use them all
"campaign_group_post_battle_looted_pooled_resources_tables": ['unknown0', 'unknown1', 'unknown2', 'unknown3', 'unknown4', 'unknown5', 'unknown6', 'unknown7'], # Too many unique columns, will use them all
"campaign_group_racial_suitability_effects_tables": ['unknown0', 'unknown1'], # Too many unique columns, will use them all
"campaign_group_rituals_tables": ['unknown0', 'unknown1'], # has no unique columns, will check column groups instead
"campaign_group_ritual_chains_tables": ['unknown0', 'unknown1'], # Too many unique columns, will use them all
"campaign_group_settlement_occupation_looted_pooled_resources_tables": ['unknown0', 'unknown1', 'unknown2', 'unknown3', 'unknown4', 'unknown5', 'unknown6', 'unknown7'], # Too many unique columns, will use them all
"campaign_group_unique_agents_tables": ['base_charges', 'campaign_group', 'unique_agent'], # Too many unique columns, will use them all
"campaign_hidden_settlement_overrides_tables": ['region'], 
"campaign_initial_loyalty_distribution_tables": ['unknown1'], 
"campaign_interactable_marker_infos_tables": ['unknown0', 'unknown1'], # Too many unique columns, will use them all
"campaign_map_attritions_tables": ['key'], 
"campaign_map_attrition_damages_tables": ['key'], 
"campaign_map_attrition_faction_immunities_tables": ['attrition', 'faction'], # has no unique columns, will check column groups instead
"campaign_map_attrition_unit_immunities_tables": ['attrition', 'unit'], # has no unique columns, will check column groups instead
"campaign_map_masks_tables": ['mask_name'], 
"campaign_map_masks_to_excluded_regions_tables": ['excluded_region', 'mask'], # Too many unique columns, will use them all
"campaign_map_playable_areas_tables": ['index', 'unknown10'], # Too many unique columns, will use them all
"campaign_map_regions_tables": ['campaign_map', 'region'], # has no unique columns, will check column groups instead
"campaign_map_roads_tables": ['key'], 
"campaign_map_settlements_tables": ['settlement_id'], 
"campaign_map_tooltips_tables": ['select_context', 'over_context'], # has no unique columns, will check column groups instead
"campaign_map_winds_of_magic_areas_tables": ['key'], 
"campaign_map_winds_of_magic_persistent_region_strengths_tables": ['region'], 
"campaign_map_winds_of_magic_strengths_tables": ['key'], 
"campaign_markers_tables": ['unknown2'], 
"campaign_mercenary_unit_character_level_restrictions_tables": ['unit'], 
"campaign_mounts_tables": ['animation_set'], 
"campaign_mount_animation_set_overrides_tables": ['character_animation_set', 'mount_unit', 'mount_unit', 'rider_animation_set'], # has no unique columns, will check column groups instead
"campaign_movement_spline_materials_tables": ['unknown0', 'unknown1', 'unknown2'], # Too many unique columns, will use them all
"campaign_mp_coop_groups_tables": ['key'], 
"campaign_mp_coop_groups_to_factions_tables": ['faction'], 
"campaign_payload_ui_details_tables": ['component'], 
"campaign_politics_strings_tables": ['key'], 
"campaign_post_battle_captive_options_tables": ['unknown0', 'unknown1', 'unknown0', 'unknown2', 'unknown0', 'unknown3', 'unknown0', 'unknown4'], # has no unique columns, will check column groups instead
"campaign_public_order_populace_effects_tables": ['effect_bundle', 'populace_happiness'], # Too many unique columns, will use them all
"campaign_region_transformation_composite_scenes_tables": ['campaign_group'], 
"campaign_religious_relations_tables": ['source', 'target'], # has no unique columns, will check column groups instead
"campaign_rogue_army_groups_tables": ['key'], 
"campaign_rogue_army_group_units_tables": ['unknown1'], 
"campaign_rogue_army_leaders_tables": ['unknown0', 'unknown3'], # Too many unique columns, will use them all
"campaign_rogue_army_setups_tables": ['unknown1', 'unknown2', 'unknown1', 'unknown3'], # has no unique columns, will check column groups instead
"campaign_rogue_army_spawn_groups_tables": ['unknown1'], 
"campaign_rogue_army_spawn_locations_tables": ['unknown1'], 
"campaign_rogue_army_spawn_regions_tables": ['unknown1', 'unknown3'], # Too many unique columns, will use them all
"campaign_settlement_display_buildings_tables": ['key'], 
"campaign_settlement_display_building_culture_overlays_tables": ['unknown0', 'unknown1'], # Too many unique columns, will use them all
"campaign_settlement_display_building_ids_tables": ['key'], 
"campaign_settlement_display_building_model_ids_tables": ['id'], 
"campaign_settlement_display_building_siege_models_tables": ['blockade', 'culture'], # has no unique columns, will check column groups instead
"campaign_settlement_display_settlement_rotations_tables": ['settlement'], 
"campaign_settlement_display_sprawl_pieces_tables": ['key'], 
"campaign_stances_composite_scenes_tables": ['group', 'stance'], # has no unique columns, will check column groups instead
"campaign_stances_factions_junctions_tables": ['faction', 'stance'], # has no unique columns, will check column groups instead
"campaign_stances_tables": ['key'], 
"campaign_stance_effects_junctions_tables": [None], # has no unique columns or column groups!
"campaign_statistics_categories_tables": ['key'], 
"campaign_statistics_strings_tables": ['campaign_statistic'], 
"campaign_storms_excluded_regions_tables": ['key'], 
"campaign_storms_tables": ['unknown0', 'unknown2', 'unknown4'], # Too many unique columns, will use them all
"campaign_tree_ids_tables": ['tree_id'], 
"campaign_tree_types_tables": ['tree_type'], 
"campaign_tree_type_cultures_tables": ['culture'], 
"campaign_tree_variants_tables": ['tree_id', 'tree_type'], # has no unique columns, will check column groups instead
"campaign_tunnelling_excluded_regions_tables": ['key'], 
"campaign_unit_stat_bonuses_tables": ['bonus', 'level', 'bonus', 'threshold'], # has no unique columns, will check column groups instead
"campaign_variables_tables": ['variable_key'], 
"campaign_vfx_descriptions_tables": ['key'], 
"campaign_vfx_lookups_tables": ['key'], 
"campaign_videos_tables": ['unknown2', 'unknown3', 'unknown4'], # Too many unique columns, will use them all
"capture_point_types_tables": ['key'], 
"cdir_campaign_junctions_tables": ['key'], 
"cdir_configs_tables": ['cdir_config_key'], 
"cdir_desire_priorities_tables": ['campaign_key', 'desire_key', 'priority'], # Too many unique columns, will use them all
"cdir_events_categories_tables": ['category_key'], 
"cdir_events_dilemma_choice_details_tables": ['choice_key', 'dilemma_key'], # has no unique columns, will check column groups instead
"cdir_events_dilemma_followup_dilemmas_tables": ['followup_dilemma_key'], 
"cdir_events_dilemma_followup_missions_tables": ['dilemma_key', 'choice_key', 'choice_key', 'followup_mission_key'], # has no unique columns, will check column groups instead
"cdir_events_dilemma_incidents_tables": ['incident_key'], 
"cdir_events_dilemma_option_junctions_tables": ['id'], 
"cdir_events_dilemma_payloads_tables": ['id'], 
"cdir_events_incident_followup_dilemmas_tables": ['incident_key', 'followup_dliemma_key'], # Too many unique columns, will use them all
"cdir_events_incident_followup_incidents_tables": ['incident_key', 'followup_incident_key'], # Too many unique columns, will use them all
"cdir_events_incident_followup_missions_tables": ['incident_key'], 
"cdir_events_incident_option_junctions_tables": ['id'], 
"cdir_events_incident_payloads_tables": ['id'], 
"cdir_events_mission_followup_dilemmas_tables": ['mission_key', 'status_key'], # has no unique columns, will check column groups instead
"cdir_events_mission_followup_missions_tables": [None], # has no unique columns or column groups!
"cdir_events_mission_incidents_tables": ['mission_key', 'status_key'], # has no unique columns, will check column groups instead
"cdir_events_mission_issuer_junctions_tables": ['mission_key'], 
"cdir_events_mission_option_junctions_tables": ['id'], 
"cdir_events_mission_payloads_tables": ['id'], 
"cdir_events_options_tables": ['option_key'], 
"cdir_events_payloads_tables": ['payload_key'], 
"cdir_faction_junctions_tables": ['key'], 
"cdir_military_generator_configs_tables": ['key'], 
"cdir_military_generator_templates_tables": ['key'], 
"cdir_military_generator_template_priorities_tables": ['config_key', 'template_key'], # has no unique columns, will check column groups instead
"cdir_military_generator_template_ratios_tables": ['template_key', 'unit_group_key'], # has no unique columns, will check column groups instead
"cdir_military_generator_unit_groups_tables": ['key'], 
"cdir_military_generator_unit_qualities_tables": ['group_key', 'unit_key'], # has no unique columns, will check column groups instead
"character_experience_skill_tiers_tables": ['agent_key', 'experience_threshold', 'agent_key', 'skill_rank'], # has no unique columns, will check column groups instead
"character_skills_tables": ['key'], 
"character_skills_to_quest_ancillaries_tables": ['ancillary', 'skill'], # Too many unique columns, will use them all
"character_skill_categories_tables": ['key'], 
"character_skill_level_details_tables": ['level', 'skill_key'], # has no unique columns, will check column groups instead
"character_skill_level_to_ancillaries_junctions_tables": ['granted_ancillary'], 
"character_skill_level_to_dilemmas_junctions_tables": ['unknown1'], 
"character_skill_level_to_effects_junctions_tables": [None], # has no unique columns or column groups!
"character_skill_nodes_skill_locks_tables": ['character_skill', 'character_skill_node'], # has no unique columns, will check column groups instead
"character_skill_nodes_tables": ['key'], 
"character_skill_node_ancillary_locks_tables": ['character_skill_node'], 
"character_skill_node_links_tables": ['child_key', 'parent_key'], # has no unique columns, will check column groups instead
"character_skill_node_link_types_tables": ['link_type'], 
"character_skill_node_sets_tables": ['key', 'agent_subtype_key'], # Too many unique columns, will use them all
"character_skill_utilization_hints_junctions_tables": ['key'], 
"character_skill_utilization_hints_tables": ['key'], 
"character_traits_tables": ['key'], 
"character_trait_levels_tables": ['key'], 
"chat_shortcuts_tables": ['key'], 
"climates_tables": ['climate_type'], 
"climbing_ladders_meshes_definitions_tables": ['faction_key'], 
"combat_potentials_adjustments_for_banners_junctions_tables": ['banner', 'combat_potential_adjustment_type'], # has no unique columns, will check column groups instead
"combat_potentials_adjustment_types_tables": ['combat_potential_adjustment_type'], 
"combat_potentials_types_tables": ['combat_potential_type_key'], 
"commander_unit_permissions_tables": ['unit_key'], 
"commodities_tables": ['key'], 
"commodity_unit_names_tables": ['unit'], 
"composite_scene_files_tables": ['scene_filepath'], 
"confederation_effect_bundles_tables": ['culture', 'effect_bundle'], # Too many unique columns, will use them all
"cultures_subcultures_tables": ['subculture', 'index'], # Too many unique columns, will use them all
"cultures_tables": [None], # NO TSV FILES FOUND IN FOLDER
"culture_campaign_destruction_composite_scene_junctions_tables": ['culture'], 
"culture_packs_tables": ['unknown1'], 
"culture_pack_ids_tables": ['key'], 
"culture_settlement_occupation_options_tables": ['id'], 
"culture_to_battle_animation_tables_tables": ['battle_animations_table', 'culture'], # has no unique columns, will check column groups instead
"cursors_tables": ['key'], 
"cursor_transitions_tables": ['initiating_cursor'], 
"cursus_honorum_level_requirements_tables": ['level', 'subculture_key', 'level', 'faction_key', 'rank', 'subculture_key', 'rank', 'faction_key'], # has no unique columns, will check column groups instead
"custom_loading_screens_tables": ['unknown0'], 
"custom_loading_screen_components_tables": ['unknown0', 'unknown1', 'unknown1', 'unknown2'], # has no unique columns, will check column groups instead
"death_types_tables": ['key'], 
"deployables_abilities_tables": ['ability_key'], 
"deployables_categories_tables": ['deployable_category'], 
"deployables_custom_battles_tables": ['deployable'], 
"deployables_tables": ['key'], 
"deployment_area_displays_tables": ['key'], 
"destruction_zone_mask_types_tables": ['key'], 
"dilemmas_tables": ['key'], 
"diplomacy_components_tables": ['component'], 
"diplomacy_current_treaties_to_diplomatic_options_tables": ['current_treaty_key'], 
"diplomacy_keys_tables": ['key'], 
"diplomacy_keys_to_diplomacy_key_groups_tables": ['key'], 
"diplomacy_key_groups_tables": ['group_id'], 
"diplomacy_negotiation_attitudes_tables": ['key'], 
"diplomacy_negotiation_string_options_tables": [None], # has no unique columns or column groups!
"diplomacy_strings_tables": ['key'], 
"diplomatic_actions_tables": ['key'], 
"diplomatic_action_faction_restrictions_tables": ['faction'], 
"diplomatic_action_subculture_restrictions_tables": ['subculture'], 
"diplomatic_relations_attitudes_tables": ['attitude', 'value'], # Too many unique columns, will use them all
"diplomatic_relations_religion_tables": ['religion_a', 'religion_b'], # has no unique columns, will check column groups instead
"effects_additional_tooltip_details_tables": ['effect'], 
"effects_tables": ['effect'], 
"effect_bonus_value_agent_action_record_junctions_tables": ['effect', 'agent_action_record'], # has no unique columns, will check column groups instead
"effect_bonus_value_agent_junction_tables": ['effect', 'agent'], # has no unique columns, will check column groups instead
"effect_bonus_value_agent_subtype_junctions_tables": ['effect', 'subtype'], # has no unique columns, will check column groups instead
"effect_bonus_value_attrition_record_junctions_tables": ['attrition_record', 'effect'], # has no unique columns, will check column groups instead
"effect_bonus_value_basic_junction_tables": ['effect', 'bonus_value_id'], # has no unique columns, will check column groups instead
"effect_bonus_value_battle_context_army_special_ability_junctions_tables": ['unknown0', 'unknown1', 'unknown2'], # Too many unique columns, will use them all
"effect_bonus_value_battle_context_junctions_tables": ['bonus_value_id', 'effect_key'], # has no unique columns, will check column groups instead
"effect_bonus_value_battle_context_unit_attribute_junctions_tables": ['effect_key'], 
"effect_bonus_value_building_set_junctions_tables": ['building_set', 'effect'], # has no unique columns, will check column groups instead
"effect_bonus_value_faction_junctions_tables": ['effect', 'faction'], # has no unique columns, will check column groups instead
"effect_bonus_value_ids_unit_sets_tables": [None], # has no unique columns or column groups!
"effect_bonus_value_id_action_results_additional_outcomes_junctions_tables": ['action_results_additional_outcome_record', 'effect'], # has no unique columns, will check column groups instead
"effect_bonus_value_loyalty_event_junctions_tables": ['unknown1'], 
"effect_bonus_value_military_force_ability_junctions_tables": ['unknown1', 'unknown2'], # has no unique columns, will check column groups instead
"effect_bonus_value_name_record_junctions_tables": ['bonus_value_id', 'name_record'], # has no unique columns, will check column groups instead
"effect_bonus_value_pooled_resource_factor_junctions_tables": ['unknown1'], 
"effect_bonus_value_pooled_resource_junctions_tables": ['unknown1'], 
"effect_bonus_value_provincial_initiative_effect_record_junctions_tables": ['effect', 'effect_bonus_will_modify'], # Too many unique columns, will use them all
"effect_bonus_value_religion_junction_tables": ['effect', 'religion'], # has no unique columns, will check column groups instead
"effect_bonus_value_resource_junction_tables": ['effect', 'resource'], # Too many unique columns, will use them all
"effect_bonus_value_ritual_junctions_tables": ['unknown0', 'unknown2', 'unknown1', 'unknown2'], # has no unique columns, will check column groups instead
"effect_bonus_value_siege_item_junctions_tables": ['effect', 'siege_item'], # has no unique columns, will check column groups instead
"effect_bonus_value_special_ability_phase_record_junctions_tables": ['effect'], 
"effect_bonus_value_subculture_junctions_tables": ['effect', 'subculture'], # has no unique columns, will check column groups instead
"effect_bonus_value_unit_ability_junctions_tables": [None], # has no unique columns or column groups!
"effect_bonus_value_unit_attribute_junctions_tables": ['effect'], 
"effect_bonus_value_unit_set_unit_ability_junctions_tables": ['unit_set_ability'], 
"effect_bonus_value_unit_set_unit_attribute_junctions_tables": ['bonus_value_id', 'unit_set_attribute'], # Too many unique columns, will use them all
"effect_bundles_tables": ['key'], 
"effect_bundles_to_effects_junctions_tables": ['effect_bundle_key', 'effect_key'], # has no unique columns, will check column groups instead
"effect_bundle_advancement_stages_tables": ['key'], 
"effect_categories_tables": ['key'], 
"event_feed_categories_tables": ['category'], 
"event_feed_events_tables": ['event'], 
"event_feed_groups_tables": ['group'], 
"event_feed_group_members_tables": ['group', 'member'], # has no unique columns, will check column groups instead
"event_feed_message_events_tables": [None], # has no unique columns or column groups!
"event_feed_strings_tables": ['key'], 
"event_feed_subcategories_tables": ['subcategory'], 
"event_feed_summary_events_tables": ['event'], 
"event_feed_targeted_events_tables": ['event', 'target'], # has no unique columns, will check column groups instead
"factions_tables": ['key'], 
"factionwide_recruitment_unit_exclusions_sets_tables": ['set'], 
"factionwide_recruitment_unit_exclusions_units_sets_junctions_tables": ['unit'], 
"faction_agent_permitted_subtypes_tables": [None], # has no unique columns or column groups!
"faction_banners_tables": ['key'], 
"faction_civil_war_setups_tables": ['primary_faction', 'secondary_faction'], # Too many unique columns, will use them all
"faction_factionwide_recruitment_unit_exclusions_set_junctions_tables": ['faction'], 
"faction_features_tables": ['key'], 
"faction_feature_forests_tables": ['key'], 
"faction_feature_trees_tables": ['key'], 
"faction_feature_tree_to_transitions_tables": ['feature_set_transition'], 
"faction_groups_tables": ['key'], 
"faction_political_parties_junctions_tables": ['political_party_key'], 
"faction_rebellion_units_junctions_tables": ['faction_key', 'unit_key'], # has no unique columns, will check column groups instead
"faction_resource_consumptions_tables": ['number_of_regions', 'resource_consumption'], # Too many unique columns, will use them all
"faction_to_faction_groups_junctions_tables": ['faction_key'], 
"faction_to_mercenary_set_junctions_tables": ['faction'], 
"faction_uniform_colours_tables": ['faction_name'], 
"fame_levels_tables": ['key'], 
"fame_level_agent_record_junctions_tables": ['agent', 'fame_level'], # has no unique columns, will check column groups instead
"family_relationship_types_tables": ['relationship_type'], 
"famous_battle_pools_tables": ['pool_id', 'battle_name'], # Too many unique columns, will use them all
"feature_sets_tables": ['key'], 
"feature_set_to_faction_features_tables": ['faction_feature', 'feature_set'], # has no unique columns, will check column groups instead
"feature_set_transitions_tables": ['faction_feature_tree_to_transition'], 
"feature_set_transition_handlers_tables": ['key'], 
"feature_tree_to_feature_forests_tables": ['unknown0', 'faction_feature_tree', 'unknown0', 'unknown2'], # has no unique columns, will check column groups instead
"first_person_engines_tables": ['key'], 
"fonts_tables": ['key', 'size'], # has no unique columns, will check column groups instead
"font_names_tables": ['font_name'], 
"food_factors_tables": ['key'], 
"formations_tables": ['formation', 'icon_name', 'order'], # Too many unique columns, will use them all
"formations_to_subcultures_tables": ['formation', 'sub_culture'], # has no unique columns, will check column groups instead
"frontend_factions_tables": ['faction'], 
"frontend_faction_effect_groups_tables": ['unknown2'], 
"frontend_faction_effect_junctions_tables": ['effect', 'faction'], # has no unique columns, will check column groups instead
"frontend_faction_groups_tables": ['key'], 
"frontend_faction_groups_to_factions_tables": ['faction_key'], 
"frontend_faction_leaders_tables": ['key'], 
"frontend_faction_top_units_tables": ['faction', 'unit'], # has no unique columns, will check column groups instead
"game_area_enums_tables": ['key'], 
"geomantic_web_links_tables": ['unknown0', 'unknown1', 'unknown2', 'unknown3', 'unknown4', 'unknown5', 'unknown6'], # Too many unique columns, will use them all
"government_types_tables": ['government_type'], 
"governorships_tables": ['governorship'], 
"graphics_settings_options_tables": ['key'], 
"graphics_settings_tables": ['key'], 
"graphics_settings_to_graphics_options_junctions_tables": ['graphic_settings', 'graphic_settings_options', 'graphic_settings_options', 'unknown2'], # has no unique columns, will check column groups instead
"ground_types_tables": ['type'], 
"ground_type_stat_effect_groups_tables": ['group_name'], 
"ground_type_to_stat_effects_tables": [None], # has no unique columns or column groups!
"ground_type_to_texture_groups_tables": ['texture_group'], 
"groupings_military_tables": ['military_group'], 
"help_page_index_records_tables": ['key'], 
"honour_effects_tables": ['key'], 
"honour_factors_tables": ['key'], 
"incidents_tables": ['key'], 
"intrigue_actions_incidents_junctions_tables": ['unknown2'], 
"lab_settings_tables": ['key'], 
"land_units_additional_personalities_groups_junctions_tables": ['battle_personality', 'group'], # has no unique columns, will check column groups instead
"land_units_officers_tables": ['key'], 
"land_units_tables": ['key'], 
"land_units_to_unit_abilites_junctions_tables": ['ability', 'land_unit'], # has no unique columns, will check column groups instead
"land_unit_articulated_vehicles_tables": ['key'], 
"loading_screen_quotes_categories_tables": ['unknown0'], 
"loading_screen_quotes_tables": ['key'], 
"loading_screen_quotes_to_campaigns_tables": ['unknown0', 'unknown1'], # has no unique columns, will check column groups instead
"loading_screen_quotes_to_cultures_tables": ['unknown0', 'unknown1'], # has no unique columns, will check column groups instead
"loading_screen_quotes_to_quest_battles_tables": ['quest_battle'], 
"loading_screen_quotes_to_units_tables": ['quote', 'unit'], # has no unique columns, will check column groups instead
"loyalty_event_effects_tables": ['event'], 
"loyalty_factors_tables": ['key'], 
"main_units_tables": ['unit'], 
"melee_weapons_tables": ['key'], 
"mercenary_pools_tables": ['key'], 
"mercenary_pool_to_groups_junctions_tables": ['key'], 
"mercenary_pool_type_enums_tables": ['pool_type'], 
"mercenary_unit_groups_tables": ['key'], 
"message_events_tables": ['event'], 
"message_event_strings_tables": ['culture'], # 'key' column is not unique
"military_force_legacy_emblems_tables": ['key'], 
"military_force_legacy_names_tables": ['key', 'subculture', 'subculture', 'for_army'], # has no unique columns, will check column groups instead
"military_force_types_tables": ['unknown0'], 
"ministerial_effectiveness_modifiers_tables": ['leader_minister_level', 'government_type'], # has no unique columns, will check column groups instead
"ministerial_positions_culture_details_tables": ['unique_id'], 
"ministerial_positions_tables": ['minister_key'], 
"ministerial_position_effect_bundles_tables": ['campaign_group'], 
"ministerial_position_to_required_building_junctions_tables": ['unknown0', 'unknown1'], # Too many unique columns, will use them all
"ministerial_positition_to_subtype_restrictions_tables": ['agent_subtype', 'ministerial_position'], # has no unique columns, will check column groups instead
"missile_weapons_tables": ['key'], 
"missile_weapons_to_projectiles_tables": ['missile_weapon', 'projectile'], # Too many unique columns, will use them all
"missions_tables": ['key'], 
"mission_category_age_multipliers_tables": ['key'], 
"mission_category_thresholds_tables": ['key'], 
"mission_category_threshold_valid_subcultures_tables": ['threshold'], 
"mission_issuers_tables": ['issuer_key'], 
"mission_weights_tables": ['mission_key'], 
"models_building_tables": ['unknown3'], 
"models_deployables_tables": ['key'], 
"models_entity_weapons_tables": ['key'], 
"models_sieges_tables": ['unknown1', 'unknown2', 'unknown3'], # Too many unique columns, will use them all
"modifiable_unit_stats_tables": ['stat_key'], 
"mortuary_cult_categories_tables": ['unknown0'], 
"mortuary_cult_categories_to_rituals_tables": ['unknown1'], 
"mounts_tables": ['key'], 
"mp_budgets_tables": ['key'], 
"mp_force_gen_compositions_tables": ['key'], 
"mp_force_gen_template_junctions_tables": [None], # has no unique columns or column groups!
"names_groups_tables": ['key'], 
"names_tables": ['id'], 
"name_orders_tables": ['name_group', 'order', 'name_group', 'type'], # has no unique columns, will check column groups instead
"naval_effects_tables": ['key'], 
"naval_ramming_events_tables": ['key'], 
"naval_units_tables": ['key'], 
"naval_weapons_enums_tables": ['types'], 
"naval_weapons_tables": ['key'], 
"new_content_alerts_tables": ['key'], 
"particle_effects_tables": ['key'], 
"pdlc_tables": ['id', 'steam_id', 'description'], # Too many unique columns, will use them all
"plagues_tables": [None], # NO TSV FILES FOUND IN FOLDER
"political_actions_tables": ['political_action_key'], 
"political_parties_frontend_leaders_junctions_tables": ['frontend_leader'], 
"political_parties_tables": ['key'], 
"pooled_resources_tables": ['unknown0', 'unknown5', 'unknown6'], # Too many unique columns, will use them all
"pooled_resource_factors_tables": ['unknown0'], 
"pooled_resource_factor_junctions_tables": ['unknown0'], 
"population_classes_tables": ['population_class'], 
"prefab_types_tables": ['prefab_type', 'value'], # Too many unique columns, will use them all
"pre_battle_speeches_tables": ['key'], 
"projectiles_explosions_tables": ['key'], 
"projectiles_tables": ['key'], 
"projectile_bombardments_tables": ['bombardment_key'], 
"projectile_bombardment_launch_sources_tables": ['suggested_launch_source', 'description'], # Too many unique columns, will use them all
"projectile_displays_tables": ['key'], 
"projectile_first_person_params_tables": ['key'], 
"projectile_homing_params_tables": ['key'], 
"projectile_impacts_tables": ['key'], 
"projectile_penetration_junctions_tables": ['key'], 
"projectile_shot_type_enum_tables": ['key'], 
"projectile_shrapnels_tables": ['key'], 
"prologue_chapters_tables": ['battle_key', 'campaign_key', 'is_battle', 'number', 'banner'], # Too many unique columns, will use them all
"provinces_tables": ['key'], 
"province_to_mercenary_set_junctions_tables": ['province'], 
"provincial_initiatives_to_subculture_junctions_tables": ['provincial_initiative_key', 'subculture'], # has no unique columns, will check column groups instead
"provincial_initiative_records_tables": ['key'], 
"provincial_initiative_strength_levels_tables": ['unknown0'], 
"provincial_initiative_strength_province_to_province_junctions_tables": ['province', 'province1'], # has no unique columns, will check column groups instead
"purchasable_effects_tables": ['key'], 
"purchasable_effect_levels_tables": ['unknown1', 'unknown2', 'unknown3'], # Too many unique columns, will use them all
"quotes_people_tables": ['quote_person_key'], 
"quotes_tables": ['key'], 
"random_localisation_strings_tables": ['key'], 
"random_unlocalised_strings_tables": ['key'], 
"regions_tables": ['key'], 
"regions_to_region_groups_junctions_tables": ['region'], 
"region_groups_tables": ['group_key'], 
"region_religions_tables": ['region', 'religion'], # has no unique columns, will check column groups instead
"region_to_province_junctions_tables": ['region'], 
"region_unit_resources_tables": ['key'], 
"religions_tables": ['religion_key'], 
"religious_rebellions_tables": ['rebel_shadowed_faction', 'campaign', 'religion', 'campaign'], # has no unique columns, will check column groups instead
"resources_tables": ['key'], 
"resources_to_campaign_junctions_tables": ['campaign', 'resource'], # has no unique columns, will check column groups instead
"resource_costs_tables": ['unknown0'], 
"resource_cost_pooled_resource_junctions_tables": ['unknown2'], 
"resource_cost_trade_resource_junctions_tables": ['unknown0', 'unknown1'], # has no unique columns, will check column groups instead
"resource_ui_overrides_tables": ['unknown1'], 
"rituals_tables": ['key'], 
"rituals_to_ritual_chains_tables": ['unknown1'], 
"ritual_additional_ui_explanation_texts_tables": ['key'], 
"ritual_beams_tables": ['id'], 
"ritual_beam_types_tables": ['key'], 
"ritual_categories_tables": ['unknown0'], 
"ritual_chains_tables": ['unknown0', 'unknown3', 'unknown4'], # Too many unique columns, will use them all
"ritual_incursion_strengths_tables": ['unknown0', 'unknown1', 'unknown1', 'unknown2'], # has no unique columns, will check column groups instead
"ritual_payloads_tables": ['unknown0'], 
"ritual_payload_ancillaries_tables": ['id', 'payload', 'ancillary'], # Too many unique columns, will use them all
"ritual_payload_diplomatic_attitude_changes_tables": ['unknown1'], 
"ritual_payload_effect_bundles_tables": ['unknown0', 'unknown1'], # Too many unique columns, will use them all
"ritual_payload_resource_transactions_tables": ['unknown0'], 
"ritual_payload_spawn_agents_tables": ['unknown1', 'unknown3'], # Too many unique columns, will use them all
"ritual_payload_spawn_armies_tables": ['unknown0', 'unknown2', 'unknown3'], # Too many unique columns, will use them all
"ritual_payload_spawn_mercenaries_tables": ['id', 'payload', 'spawnable_unit'], # Too many unique columns, will use them all
"ritual_payload_spawn_storms_tables": ['unknown0', 'unknown1', 'unknown2', 'unknown3'], # Too many unique columns, will use them all
"ritual_reaction_constraints_tables": ['unknown0'], 
"scripted_objectives_tables": ['key'], 
"scripted_subtitles_tables": ['key'], 
"seasons_tables": ['season', 'onscreen'], # Too many unique columns, will use them all
"sea_surfaces_tables": ['key'], 
"settlement_abandoment_buildings_tables": ['building'], 
"settlement_climate_types_tables": ['unknown0', 'unknown1'], # Too many unique columns, will use them all
"settlement_occupation_options_tables": ['key'], 
"settlement_vandalisation_buildings_tables": ['building'], 
"ship_dbs_tables": ['key'], 
"shortcut_localisation_tables": ['key'], 
"slot_templates_tables": ['key'], 
"slot_template_to_building_superchain_junctions_tables": ['id'], 
"slot_types_tables": ['key'], 
"spawnable_forces_tables": ['key'], 
"spawnable_force_unit_list_junctions_tables": ['unknown0', 'unknown6', 'unknown7'], # Too many unique columns, will use them all
"special_ability_displays_tables": ['sa_display_key'], 
"special_ability_groups_tables": ['ability_group'], 
"special_ability_groups_to_units_junctions_tables": ['ability_group', 'unit'], # has no unique columns, will check column groups instead
"special_ability_groups_to_unit_abilities_junctions_tables": ['special_ability_groups', 'unit_special_abilities'], # has no unique columns, will check column groups instead
"special_ability_group_parents_tables": ['child'], 
"special_ability_invalid_usage_flags_tables": ['flag_key'], 
"special_ability_phases_tables": ['id'], 
"special_ability_phase_attribute_effects_tables": ['attribute', 'phase'], # has no unique columns, will check column groups instead
"special_ability_phase_displays_tables": ['key'], 
"special_ability_phase_stat_effects_tables": ['phase', 'stat'], # has no unique columns, will check column groups instead
"special_ability_to_auto_deactivate_flags_tables": ['invalid_usage_flag', 'special_ability_key'], # has no unique columns, will check column groups instead
"special_ability_to_invalid_target_flags_tables": ['invalid_target', 'special_ability'], # has no unique columns, will check column groups instead
"special_ability_to_invalid_usage_flags_tables": ['invalid_usage_flag', 'special_ability'], # has no unique columns, will check column groups instead
"special_ability_to_recharge_contexts_tables": ['special_ability'], 
"special_ability_to_special_ability_phase_junctions_tables": ['order', 'special_ability', 'phase', 'special_ability'], # has no unique columns, will check column groups instead
"stances_tables": ['key'], 
"stats_tables": ['key'], 
"subculture_settlement_occupation_effect_bundle_suitabilities_tables": ['climate', 'suitability'], # Too many unique columns, will use them all
"subculture_settlement_occupation_suitability_types_tables": ['key'], 
"subculture_treasure_hunt_dilemma_categories_tables": ['dilemma_category'], 
"subtitle_timings_tables": [None], # has no unique columns or column groups!
"taxes_classes_tables": ['tax'], 
"taxes_effects_jct_tables": ['tax_name', 'effect'], # has no unique columns, will check column groups instead
"taxes_keys_tables": ['tax_level', 'tax_lookup'], # Too many unique columns, will use them all
"taxes_levels_tables": ['tax_level', 'percentage'], # Too many unique columns, will use them all
"technologies_tables": ['key'], 
"technology_categories_tables": ['key'], 
"technology_category_modules_tables": ['max_tier', 'technology_node_set', 'min_tier', 'technology_node_set'], # has no unique columns, will check column groups instead
"technology_character_traits_junctions_tables": ['unknown0', 'unknown1'], # Too many unique columns, will use them all
"technology_effects_junction_tables": ['technology', 'effect'], # has no unique columns, will check column groups instead
"technology_nodes_tables": ['key'], 
"technology_nodes_to_ancillaries_junctions_tables": ['technology_node', 'ancillary'], # Too many unique columns, will use them all
"technology_node_links_tables": ['child_key', 'parent_key'], # has no unique columns, will check column groups instead
"technology_node_sets_tables": ['key'], 
"technology_required_building_levels_junctions_tables": ['technology', 'required_bulding_level'], # has no unique columns, will check column groups instead
"technology_required_technology_junctions_tables": ['technology', 'required_technology'], # has no unique columns, will check column groups instead
"technology_ui_groups_tables": ['key'], 
"technology_ui_groups_to_technology_nodes_junctions_tables": [None], # NO TSV FILES FOUND IN FOLDER
"trade_node_groups_tables": ['key'], 
"trait_categories_tables": ['category', 'icon_path'], # Too many unique columns, will use them all
"trait_info_tables": ['trait'], 
"trait_level_effects_tables": ['trait_level', 'effect'], # has no unique columns, will check column groups instead
"trait_to_antitraits_tables": ['trait'], 
"trigger_events_tables": ['event'], 
"ui_colours_tables": ['key'], 
"ui_colour_profiles_tables": ['key'], 
"ui_colour_profile_colour_overrides_tables": ['unknown0', 'green', 'unknown0', 'ui_colour_profile'], # has no unique columns, will check column groups instead
"ui_large_images_tables": ['image_path'], 
"ui_tagged_images_tables": ['key'], 
"ui_text_replacements_tables": ['key'], 
"ui_tooltips_tables": ['key'], 
"ui_tooltip_components_tables": ['child_id', 'ui_tooltip'], # has no unique columns, will check column groups instead
"ui_unit_bullet_points_generations_tables": [None], # has no unique columns or column groups!
"ui_unit_bullet_point_enums_tables": ['key'], 
"ui_unit_bullet_point_unit_overrides_tables": ['bullet_point', 'unit_key'], # has no unique columns, will check column groups instead
"ui_unit_groupings_tables": ['key'], 
"ui_unit_group_parents_tables": ['key'], 
"ui_unit_stats_filters_tables": ['key'], 
"ui_unit_stats_tables": ['key'], 
"ui_unit_statuses_tables": ['key'], 
"ui_unit_stat_to_classes_tables": ['stat_key', 'unit_class', 'unit_class', 'list_order'], # has no unique columns, will check column groups instead
"ui_unit_stat_to_unit_castes_tables": ['stat', 'unit_caste'], # has no unique columns, will check column groups instead
"unique_agents_tables": ['agent_subtype', 'clan_name', 'forename', 'other_name', 'surname', 'agent_type', 'spawn_via_ui'], # Too many unique columns, will use them all
"unique_agent_component_junctions_tables": ['component', 'unique_agent'], # has no unique columns, will check column groups instead
"unique_agent_spawn_vfx_junctions_tables": ['composite_scene', 'unique_agent'], # Too many unique columns, will use them all
"units_custom_battle_mounts_tables": ['mounted_unit'], 
"units_custom_battle_permissions_tables": ['faction', 'unit'], # has no unique columns, will check column groups instead
"units_to_exclusive_faction_permissions_tables": ['key', 'faction'], # has no unique columns, will check column groups instead
"units_to_groupings_military_permissions_tables": ['unit', 'military_group'], # has no unique columns, will check column groups instead
"unit_abilities_additional_ui_effects_tables": ['key'], 
"unit_abilities_tables": ['key'], 
"unit_abilities_to_additional_ui_effects_juncs_tables": ['ability', 'effect'], # has no unique columns, will check column groups instead
"unit_ability_source_types_tables": ['key'], 
"unit_ability_types_tables": ['key'], 
"unit_armour_types_tables": [None], # NO TSV FILES FOUND IN FOLDER
"unit_attributes_groups_tables": ['group_name'], 
"unit_attributes_tables": ['key'], 
"unit_attributes_to_groups_junctions_tables": ['attribute', 'attribute_group'], # has no unique columns, will check column groups instead
"unit_banners_tables": ['key'], 
"unit_banner_unit_height_offsets_tables": [None], # NO TSV FILES FOUND IN FOLDER
"unit_castes_tables": ['caste', 'localised_name'], # Too many unique columns, will use them all
"unit_category_tables": ['key'], 
"unit_class_tables": ['key'], 
"unit_description_historical_texts_tables": ['key'], 
"unit_description_short_texts_tables": ['key'], 
"unit_description_strengths_weaknesses_texts_tables": ['key'], 
"unit_experience_bonuses_tables": ['stat', 'growth_scalar'], # Too many unique columns, will use them all
"unit_experience_thresholds_tables": ['key'], 
"unit_fatigue_effects_tables": ['fatigue_level', 'stat'], # has no unique columns, will check column groups instead
"unit_lists_tables": ['key'], 
"unit_porthole_camera_settings_tables": ['key'], 
"unit_required_technology_junctions_tables": ['unit_key', 'technology_key'], # Too many unique columns, will use them all
"unit_sets_tables": ['unknown0'], 
"unit_set_to_unit_junctions_tables": [None], # has no unique columns or column groups!
"unit_set_unit_ability_junctions_tables": ['key'], 
"unit_set_unit_attribute_junctions_tables": ['key'], 
"unit_shield_types_tables": ['key'], 
"unit_spacings_tables": ['key'], 
"unit_special_abilities_tables": ['key'], 
"unit_stats_land_experience_bonuses_tables": ['xp_level', 'mp_fixed_cost', 'mp_experience_cost_multiplier', 'additional_melee_cp', 'additional_missile_cp'], # Too many unique columns, will use them all
"unit_stats_naval_experience_bonuses_tables": ['xp_level', 'melee_defence', 'melee_attack', 'core_gunner_marksmanship', 'mp_fixed_cost', 'mp_experience_cost_multiplier'], # Too many unique columns, will use them all
"unit_stat_localisations_tables": ['stat_key'], 
"unit_stat_modifiers_tables": ['key'], 
"unit_to_unit_list_junctions_tables": ['unit', 'unit_list'], # has no unique columns, will check column groups instead
"unit_variants_colours_tables": ['key'], 
"unit_variants_ships_tables": ['name', 'unit', 'unit_card'], # Too many unique columns, will use them all
"unit_variants_tables": ['faction', 'unit'], # has no unique columns, will check column groups instead
"unit_weights_tables": ['key'], 
"vampire_mercenary_set_junctions_tables": ['mercenary_set'], 
"variants_tables": ['variant_name'], 
"victory_conditions_tables": ['condition'], 
"victory_types_tables": ['victory_type'], 
"victory_type_links_tables": ['from', 'to'], # Too many unique columns, will use them all
"videos_tables": ['video_name'], 
"warscape_animated_lod_tables": ['key'], 
"warscape_animated_tables": ['key'], 
"wind_levels_tables": ['key'], 
"_kv_battle_ai_ability_usage_variables_tables": ['key'], 
"_kv_experience_bonuses_tables": ['key'], 
"_kv_fatigue_tables": ['key'], 
"_kv_fire_values_tables": ['key'], 
"_kv_key_buildings_tables": ['key'], 
"_kv_morale_tables": ['key'], 
"_kv_naval_morale_tables": ['key'], 
"_kv_naval_rules_tables": ['key'], 
"_kv_rules_tables": ['key'], 
"_kv_ui_tweakers_tables": ['key'], 
"_kv_unit_ability_scaling_rules_tables": ['key'], 
"_kv_winds_of_magic_params_tables": ['key'], 
}
#END OF FILE