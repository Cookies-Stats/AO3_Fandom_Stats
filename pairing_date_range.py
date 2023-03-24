import datetime

#Ask user whether they want to use a file or input a single pairing
use_file = input("Do you want to use the pairings.txt file? (Y/N): ").strip().lower()

#Read the pairings from a text file or accept a single pairing as input
if use_file =="y":
	with open("pairings.txt", "r", encoding='utf-8') as file:
		pairings = [line.strip() for line in file]
else:
	single_pairing = input("Enter a single pairing: ")
	pairings = [single_pairing]

start_date_input = input("Enter the start date (YYYY-MM-DD): ")
end_date_input = input("Enter the end date (YYYY-MM-DD): ")

start_date = datetime.datetime.strptime(start_date_input, "%Y-%m-%d").date()
end_date = datetime.datetime.strptime(end_date_input, "%Y-%m-%d").date()

base_url = "https://archiveofourown.org/works/search?commit=Search&work_search%5Bquery%5D=created_at%3A%5B%22{start_date}%22+TO+%22{end_date}%22%5D&work_search%5Btitle%5D=&work_search%5Bcreators%5D=&work_search%5Brevised_at%5D=&work_search%5Bcomplete%5D=&work_search%5Bcrossover%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bword_count%5D=&work_search%5Blanguage_id%5D=&work_search%5Bfandom_names%5D=&work_search%5Brating_ids%5D=&work_search%5Bcharacter_names%5D=&work_search%5Brelationship_names%5D={pairing}&work_search%5Bfreeform_names%5D=&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Bcomments_count%5D=&work_search%5Bbookmarks_count%5D=&work_search%5Bsort_column%5D=title_to_sort_on&work_search%5Bsort_direction%5D=desc"
otp_url = "https://archiveofourown.org/works/search?commit=Search&work_search%5Bquery%5D=created_at%3A%5B%22{start_date}%22+TO+%22{end_date}%22%5D +otp%3Atrue&work_search%5Btitle%5D=&work_search%5Bcreators%5D=&work_search%5Brevised_at%5D=&work_search%5Bcomplete%5D=&work_search%5Bcrossover%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bword_count%5D=&work_search%5Blanguage_id%5D=&work_search%5Bfandom_names%5D=&work_search%5Brating_ids%5D=&work_search%5Bcharacter_names%5D=&work_search%5Brelationship_names%5D={pairing}&work_search%5Bfreeform_names%5D=&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Bcomments_count%5D=&work_search%5Bbookmarks_count%5D=&work_search%5Bsort_column%5D=title_to_sort_on&work_search%5Bsort_direction%5D=desc"

urls = [base_url, otp_url]

url_categories = [
	("All Pairing Count", base_url),
	("One True Pairing", otp_url),
]

with open("urls.txt", "w", encoding='utf-8') as file:
	for pairing in pairings:
		encoded_pairing = pairing.replace(" ", "+").replace("|", "%7C").replace("/", "%2F").replace("&", "%26")
		for category, url_template in url_categories:
			url = url_template.format(pairing=encoded_pairing, start_date=start_date, end_date=end_date)
			file.write(f"{pairing}\t{category}\t{url}\n")

print("URLs saved to urls.txt")
