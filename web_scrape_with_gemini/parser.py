import google.generativeai as genai
import os

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

def parse_with_gemini(dom_chunks, parse_description):
    model = genai.GenerativeModel("gemini-1.5-flash")

    parsed_results = []
    for i,chunk in enumerate(dom_chunks,start=1):
        response = model.generate_content(
            prompt =template.format(dom_chunks=chunk,parse_description=parse_description)
        )
        print(f"parsed match:{i} of {len(dom_chunks)}")
        parsed_results.append(response)
        
    return "\n".join(parsed_results)
    