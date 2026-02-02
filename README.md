

# 📋 Team Task Tracker API

**Team Task Tracker** არის კომპანიის შიდა მინი-სისტემა, რომელიც გუნდებს ეხმარება ყოველდღიური სამუშაოების მართვაში. პროექტის მთავარი ფოკუსია მონაცემთა უსაფრთხოება და იზოლაცია: თითოეული თანამშრომელი ხედავს და მართავს მხოლოდ იმ დავალებებს, რომლებიც მის გუნდს ეკუთვნის.

## 🚀 ძირითადი ფუნქციონალი
*   **Multi-tenant Access Control:** მომხმარებლებს აქვთ წვდომა მხოლოდ საკუთარი გუნდის მონაცემებზე (Object-level access).
*   **JWT Authentication:** უსაფრთხო ავტორიზაცია JSON Web Tokens-ის გამოყენებით.
*   **Task Management (CRUD):** დავალებების შექმნა, ნახვა, განახლება და წაშლა.
*   **Advanced Filtering:** დავალებების ფილტრაცია სტატუსის (`is_done`) და თეგების მიხედვით.
*   **Query Optimization:** გამოყენებულია `select_related` და `prefetch_related` N+1 პრობლემის თავიდან ასაცილებლად.
*   **Custom Django Admin:** გაფართოებული ადმინ-პანელი ძებნისა და ფილტრაციის ფუნქციით.

## 🛠 ტექნოლოგიური სთეკი
*   **Framework:** Django, Django REST Framework (DRF)
*   **Auth:** SimpleJWT
*   **Database:** SQLite (Development)
*   **Tools:** Django-filter, Python 3.x

## 🏗 მონაცემთა მოდელი
*   **Team:** გუნდების მართვა (მაგ: Backend, Frontend, Sales).
*   **Profile:** მომხმარებლის კავშირი გუნდთან და მისი როლი.
*   **Task:** დავალება, რომელიც მიბმულია კონკრეტულ გუნდზე, შემსრულებელზე და თეგებზე.
*   **Tag:** დავალებების კატეგორიზაცია (მაგ: "Urgent", "Bug").

## 🔌 API Endpoints

### აუთენტიფიკაცია
*   `POST /api/token/` - ტოკენის მიღება (Login)
*   `POST /api/token/refresh/` - ტოკენის განახლება

### დავალებები (Tasks)
*   `GET /api/tasks/` - გუნდის დავალებების სია (Pagination, Filtering, Ordering)
*   `POST /api/tasks/` - ახალი დავალების შექმნა
*   `GET /api/tasks/{id}/` - დავალების დეტალები
*   `PATCH /api/tasks/{id}/` - დავალების ნაწილობრივი განახლება
*   `DELETE /api/tasks/{id}/` - დავალების წაშლა

### სხვა
*   `GET /health/` - სისტემის სტატუსის შემოწმება
*   `GET /about/` - ინფორმაცია API-ს შესახებ

