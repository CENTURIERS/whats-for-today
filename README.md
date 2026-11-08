# whats-for-today
System zawierający przepisy i wspierający wymyślanie dań. Dlaczego taki system? a to dlatego, że każdy z nas zastanawia się co dzisiaj na obiad, co kupić albo co zrobić z tego co mam bo 10-ty za rogiem ahahha


# Schemat Bazy Danych (ERD)

```mermaid
erDiagram
    %% --- RELACJE ---
    USER ||--o{ RECIPE : "tworzy"
    USER ||--o{ RATING : "wystawia"
    USER ||--o{ COMMENT : "publikuje"
    USER ||--o{ MEAL_PLAN : "planuje"
    USER ||--o{ PASSWORD_RESET_TOKEN : "posiada"
    USER ||--o{ EMAIL_VERIFICATION_TOKEN : "posiada"

    CATEGORY ||--o{ RECIPE : "klasyfikuje"

    RECIPE ||--o{ RECIPE_STEP : "zawiera"
    RECIPE ||--o{ RECIPE_INGREDIENT : "wymaga"
    RECIPE ||--o{ RECIPE_TAG : "posiada"
    RECIPE ||--o{ RATING : "otrzymuje"
    RECIPE ||--o{ COMMENT : "zbiera"
    RECIPE ||--o{ MEAL_PLAN : "uwzględniony w"

    INGREDIENT ||--o{ RECIPE_INGREDIENT : "wykorzystany w"
    TAG ||--o{ RECIPE_TAG : "przypisany do"
    COMMENT ||--o{ COMMENT : "odpowiedź do"

    %% --- DEFINICJE TABEL ---
    USER {
        int id PK
        string nickname
        string email
        string hashed_password
        string firstname
        string surname
        string photo_url
        datetime created_at
        datetime updated_at
        datetime deleted_at
        boolean is_active
    }

    RECIPE {
        int id PK
        int user_id FK
        int category_id FK
        string name
        string description
        int estimated_time
        int portions
        string introduction
        string summary
        float rating_number
        string photo_url
        datetime created_at
        datetime updated_at
        datetime deleted_at
    }

    CATEGORY {
        int id PK
        string name
        string description
    }

    RECIPE_STEP {
        int id PK
        int recipe_id FK
        int step_number
        string instructions
    }

    INGREDIENT {
        int id PK
        string name
        string origin
        string type
        string description
        string photo_url
    }

    RECIPE_INGREDIENT {
        int recipe_id FK
        int ingredient_id FK
        float amount
        string unit
    }

    TAG {
        int id PK
        string name
        string description
        string color
        string emoji
    }

    RECIPE_TAG {
        int recipe_id FK
        int tag_id FK
    }

    RATING {
        int id PK
        int user_id FK
        int recipe_id FK
        int rating
        string topic
        string description
        string photo_url
        datetime created_at
        datetime updated_at
        datetime deleted_at
    }

    COMMENT {
        int id PK
        int user_id FK
        int recipe_id FK
        int comment_parent_id FK
        string topic
        string description
        string photo_url
        datetime created_at
        datetime updated_at
        datetime deleted_at
    }

    MEAL_PLAN {
        int id PK
        int user_id FK
        int recipe_id FK
        date planned_date
        string meal_type
    }

    PASSWORD_RESET_TOKEN {
        int id PK
        int user_id FK
        string token
        datetime expires_at
        datetime used_at
        datetime created_at
    }

    EMAIL_VERIFICATION_TOKEN {
        int id PK
        int user_id FK
        string token
        datetime expires_at
        datetime used_at
        datetime created_at
    }
```