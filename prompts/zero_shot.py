ZERO_SHOT_PROMPT = """
    
    Generate a quiz on the topic of {input}. 
    
    Include a variety of question types such as multiple choice, true/false. 
    
    Ensure that the questions are clear and concise.

    start at level 1 and work up the difficulty after each correctly answered question

    the quiz should be 10 questions long

    Include interesting facts or trivia related to each question to make the quiz more engaging.

    After each correctly answered question, provide a positive reinforcement message and a fun fact related to the question's topic.

    Vary the difficulty level of questions, starting easy and gradually increasing complexity.

    Incorporate questions that require critical thinking or application of knowledge, not just memorization.

    Include at least one question that involves a hypothetical scenario or problem-solving situation.

    Add a "bonus round" question at the end that is more challenging but offers extra points.

    Ensure that the answer choices for multiple-choice questions are plausible and not obviously incorrect.

    Include a mix of questions covering different aspects of the topic to provide a comprehensive quiz experience.

    For some questions, add brief explanations for why the correct answer is right and why other options are wrong.

    End the quiz with an encouraging message that summarizes the user's performance and encourages further learning on the topic.

{format_instructions}
"""
