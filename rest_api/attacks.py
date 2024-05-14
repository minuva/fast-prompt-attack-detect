from last_layer import scan_llm, scan_prompt, Threat

exclude = [Threat.MixedLangMarker]


def get_user_agent_attack(llm_input, llm_output) -> dict:

    user_threats = scan_prompt(llm_input, exclude)
    agent_threats = scan_llm(llm_output, exclude)

    user_markers, user_score = user_threats.markers, user_threats.score
    agent_markers, agent_score = agent_threats.markers, agent_threats.score

    user_threats = {f"user_threat_{k}": v for k, v in user_markers.items()}
    agent_threats = {f"agent_threat_{k}": v for k, v in agent_markers.items()}

    threats = {**user_threats, **agent_threats}

    if user_score:
        threats["user_threat_score"] = user_score
    
    if agent_score:
        threats["agent_threat_score"] = agent_score

    return threats