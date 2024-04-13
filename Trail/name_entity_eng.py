import spacy
import csv

def process_sentences(input_file, output_file):
    # Load spaCy's English NER model
    nlp = spacy.load("en_core_web_sm")

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
