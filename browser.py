class PageNode:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:
    def __init__(self):
        self.current = None

    def visit(self, url):
        new_page = PageNode(url)
        if self.current:
            self.current.next = new_page
            new_page.prev = self.current
        self.current = new_page
        print(f"Visited: {url}")

    def back(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            print(f"Moved Back to: {self.current.url}")
        else:
            print("No previous page to go back to.")

    def forward(self):
        if self.current and self.current.next:
            self.current = self.current.next
            print(f"Moved Forward to: {self.current.url}")
        else:
            print("No forward page to go to.")

    def show_current_page(self):
        if self.current:
            print(f"Current Page: {self.current.url}")
        else:
            print("No pages visited yet.")

    def show_history(self):
        temp = self.current
        while temp and temp.prev:
            temp = temp.prev

        print("\n📖 Browsing History:")
        while temp:
            marker = " <-- Current" if temp == self.current else ""
            print(f"- {temp.url}{marker}")
            temp = temp.next
        print()

# === TESTING / USER MENU ===
if __name__ == "__main__":
    browser = BrowserHistory()

    while True:
        print("\n=== Browser Navigation ===")
        print("1. Visit New Page")
        print("2. Go Back")
        print("3. Go Forward")
        print("4. Show Current Page")
        print("5. Show History")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            url = input("Enter URL to visit: ")
            browser.visit(url)
        elif choice == '2':
            browser.back()
        elif choice == '3':
            browser.forward()
        elif choice == '4':
            browser.show_current_page()
        elif choice == '5':
            browser.show_history()
        elif choice == '6':
            print("Exiting browser...")
            break
        else:
            print("Invalid choice. Try again.")
