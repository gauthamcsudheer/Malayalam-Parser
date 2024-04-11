import spacy
import csv

def process_sentences(input_file, output_file):
    # Load spaCy's Malayalam NER model if available
    try:
        nlp = spacy.load("xx_ent_wiki_sm")  # Load Malayalam NER model
    except OSError:
        print("Malayalam NER model not found. Please install it using 'python -m spacy download xx_ent_wiki_sm'.")
        return

    # Open input and output files
    with open(input_file, 'r', encoding='utf-8') as f_input, \
            open(output_file, 'w', newline='', encoding='utf-8') as f_output:
        csv_writer = csv.writer(f_output)
        csv_writer.writerow(['Sentence', 'Entity', 'Label'])  # Write header row

        # Process each sentence in the input file
        for line in f_input:
            line = line.strip()
            if line:
                doc = nlp(line)
                for ent in doc.ents:
                    csv_writer.writerow([line, ent.text, ent.label_])

if __name__ == "__main__":
    input_file = input("Enter the path to the input text file: ")
    output_file = input("Enter the path to save the output CSV file: ")

    process_sentences(input_file, output_file)
    print("Tagged dataset has been saved to", output_file)
