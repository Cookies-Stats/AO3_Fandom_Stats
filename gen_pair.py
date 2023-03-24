base_url = "https://archiveofourown.org/works/search?commit=Search&work_search%5Bquery%5D=created_at%3A%5B%222023-02-01%22+TO+%222023-02-28%22%5D&work_search%5Btitle%5D=&work_search%5Bcreators%5D=&work_search%5Brevised_at%5D=&work_search%5Bcomplete%5D=&work_search%5Bcrossover%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bword_count%5D=&work_search%5Blanguage_id%5D=&work_search%5Bfandom_names%5D=&work_search%5Brating_ids%5D=&work_search%5Bcharacter_names%5D=&work_search%5Brelationship_names%5D={pairing}&work_search%5Bfreeform_names%5D=&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Bcomments_count%5D=&work_search%5Bbookmarks_count%5D=&work_search%5Bsort_column%5D=title_to_sort_on&work_search%5Bsort_direction%5D=desc"

# Read pairings from a text file
with open("pairings.txt", "r", encoding='utf-8') as file:
    pairings = [line.strip() for line in file]

with open("urls.txt", "w", encoding='utf-8') as file:
    for pairing in pairings:
        url = base_url.format(pairing=pairing.replace(" ", "+").replace("|", "%7C").replace("/", "%2F"))
        file.write(url + "\n")

print("URLs saved to urls.txt")
