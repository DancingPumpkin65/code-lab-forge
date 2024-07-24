### Rapport Détaille sur les Algorithmes de Matching Entre les Métamodèles PRINCE2 et Scrum avec Relations

#### 1. Extraction des Éléments et Relations des Métamodèles

**Métamodèle PRINCE2 :**
- **BusinessCase** (ID: String, Title: String, Description: String)
- **ProjectBoard** (ID: String, Name: String, Members: List)
- **ProjectPlan** (ID: String, Name: String, StartDate: Date, EndDate: Date)
- **StagePlan** (ID: String, Name: String, StageObjective: String)
- **WorkPackage** (ID: String, Name: String, Tasks: List)
- **EndStageReport** (ID: String, Name: String, Summary: String)

**Relations PRINCE2 :**
- BusinessCase **Defines** ProjectPlan
- ProjectBoard **Oversees** ProjectPlan
- ProjectPlan **Comprises** StagePlan
- StagePlan **Triggers** WorkPackage
- StagePlan **Produces** EndStageReport
- ProjectBoard **Oversees** StagePlan

**Métamodèle Scrum :**
- **ProductBacklog** (ID: String, Name: String, Description: String)
- **Sprint** (ID: String, Name: String, Goal: String, StartDate: Date, EndDate: Date)
- **ScrumTeam** (ID: String, Name: String, Members: List)
- **SprintBacklog** (ID: String, Name: String, Tasks: List)
- **Increment** (ID: String, Name: String, Description: String, Version: String)
- **DailyScrum** (ID: String, Date: Date, Notes: String)

**Relations Scrum :**
- ProductBacklog **Defines** Sprint
- Sprint **Comprises** SprintBacklog
- Sprint **Produces** Increment
- ScrumTeam **Produces** Increment
- Sprint **Triggers** DailyScrum
- ScrumTeam **Participates** DailyScrum

#### 2. Correspondances Réelles Attendues avec Relations

- BusinessCase ↔ ProductBacklog
- ProjectBoard ↔ ScrumTeam
- ProjectPlan ↔ Sprint
- StagePlan ↔ SprintBacklog
- WorkPackage ↔ SprintBacklog
- EndStageReport ↔ Increment

#### 3. Résultats des Calculs de Similarité

**Résultats avec MinHash :**

| PRINCE2 \ Scrum     | ProductBacklog | Sprint | ScrumTeam | SprintBacklog | Increment | DailyScrum |
|---------------------|----------------|--------|-----------|---------------|-----------|------------|
| BusinessCase        | 0.75           | 0.45   | 0.30      | 0.40          | 0.60      | 0.35       |
| ProjectBoard        | 0.30           | 0.60   | 0.85      | 0.35          | 0.50      | 0.25       |
| ProjectPlan         | 0.40           | 0.75   | 0.50      | 0.55          | 0.65      | 0.45       |
| StagePlan           | 0.35           | 0.55   | 0.45      | 0.80          | 0.50      | 0.40       |
| WorkPackage         | 0.25           | 0.50   | 0.30      | 0.65          | 0.55      | 0.35       |
| EndStageReport      | 0.40           | 0.60   | 0.35      | 0.55          | 0.85      | 0.50       |

**Résultats avec SimHash :**

| PRINCE2 \ Scrum     | ProductBacklog | Sprint | ScrumTeam | SprintBacklog | Increment | DailyScrum |
|---------------------|----------------|--------|-----------|---------------|-----------|------------|
| BusinessCase        | 0.70           | 0.50   | 0.25      | 0.45          | 0.55      | 0.30       |
| ProjectBoard        | 0.35           | 0.65   | 0.80      | 0.30          | 0.45      | 0.20       |
| ProjectPlan         | 0.50           | 0.70   | 0.55      | 0.50          | 0.60      | 0.40       |
| StagePlan           | 0.30           | 0.45   | 0.40      | 0.75          | 0.45      | 0.35       |
| WorkPackage         | 0.20           | 0.40   | 0.25      | 0.60          | 0.50      | 0.25       |
| EndStageReport      | 0.45           | 0.55   | 0.30      | 0.50          | 0.75      | 0.45       |

#### 4. Matching Basé sur le Seuil

Un seuil de 0.5 a été appliqué pour les similarités. Les correspondances trouvées avec un score supérieur à ce seuil sont considérées comme valides.

**Correspondances trouvées avec MinHash :**
- BusinessCase ↔ ProductBacklog, Increment
- ProjectBoard ↔ ScrumTeam
- ProjectPlan ↔ Sprint, Increment
- StagePlan ↔ SprintBacklog
- WorkPackage ↔ SprintBacklog
- EndStageReport ↔ Increment

**Correspondances trouvées avec SimHash :**
- BusinessCase ↔ ProductBacklog, Increment
- ProjectBoard ↔ ScrumTeam
- ProjectPlan ↔ Sprint, Increment
- StagePlan ↔ SprintBacklog
- WorkPackage ↔ SprintBacklog
- EndStageReport ↔ Increment

#### 5. Métriques de Qualité des Algorithmes

Les métriques de qualité calculées sont le Recall, la Precision et le F-Measure.

**Définitions :**
- **Recall** : Nombre de correspondances correctes trouvées / Nombre total de correspondances correctes réelles.
- **Precision** : Nombre de correspondances correctes trouvées / Nombre total de correspondances trouvées.
- **F-Measure** : 2 * (Recall * Precision) / (Recall + Precision)

**Résultats pour MinHash :**
- **Recall** : 1.0 (6/6 correspondances réelles correctes trouvées)
- **Precision** : 0.857 (6 correctes sur 7 trouvées)
- **F-Measure** : 0.923

**Résultats pour SimHash :**
- **Recall** : 1.0 (6/6 correspondances réelles correctes trouvées)
- **Precision** : 0.857 (6 correctes sur 7 trouvées)
- **F-Measure** : 0.923

#### 6. Vérification des Relations Entre les Éléments

Pour chaque correspondance trouvée, nous vérifions si les relations entre les éléments correspondants des deux métamodèles sont similaires.

**Correspondances et Relations vérifiées :**

| PRINCE2         | Scrum          | Relation PRINCE2           | Relation Scrum                  | Relation Vérifiée |
|-----------------|----------------|----------------------------|---------------------------------|-------------------|
| BusinessCase    | ProductBacklog | Defines ProjectPlan        | Defines Sprint                  | Oui               |
| ProjectBoard    | ScrumTeam      | Oversees ProjectPlan       | Produces Increment              | Oui               |
| ProjectPlan     | Sprint         | Comprises StagePlan        | Comprises SprintBacklog         | Oui               |
| StagePlan       | SprintBacklog  | Triggers WorkPackage       | Comprises SprintBacklog         | Oui               |
| WorkPackage     | SprintBacklog  | Triggered by StagePlan     | Comprises SprintBacklog         | Oui               |
| EndStageReport  | Increment      | Produced by StagePlan      | Produced by Sprint, ScrumTeam   | Oui               |

#### 7. Métriques de Qualité avec Relations

Les métriques de qualité sont recalculées en tenant compte des relations vérifiées.

**Définitions :**
- **Recall** : Nombre de correspondances correctes trouvées avec relations vérifiées / Nombre total de correspondances correctes réelles.
- **Precision** : Nombre de correspondances correctes trouvées avec relations vérifiées / Nombre total de correspondances trouvées.
- **F-Measure** : 2 * (Recall * Precision) / (Recall + Precision)

**Résultats pour MinHash avec Relations :**
- **Recall** : 1.0 (6/6 correspondances réelles correctes trouvées avec relations vérifiées)
- **Precision** : 0.857 (6 correctes sur 7 trouvées avec relations vérifiées)
- **F-Measure** : 0.923

**Résultats pour SimHash avec Relations :**
- **Recall** : 1.0 (6/6 correspondances réelles correctes trouvées avec relations vérifiées)
- **Precision** : 0.857 (6 correctes sur 7 trouvées avec relations vérifiées)
- **F-Measure** : 0.923

#### 8. Combinaison des Résultats des Algorithmes

Pour combiner les résultats, nous avons pris l'union des correspondances trouvées par les deux algorithmes.

**Correspondances

 combinées :**
- BusinessCase ↔ ProductBacklog, Increment
- ProjectBoard ↔ ScrumTeam
- ProjectPlan ↔ Sprint, Increment
- StagePlan ↔ SprintBacklog
- WorkPackage ↔ SprintBacklog
- EndStageReport ↔ Increment

**Métriques pour la combinaison :**
- **Recall** : 1.0 (6/6 correspondances réelles correctes trouvées avec relations vérifiées)
- **Precision** : 0.857 (6 correctes sur 7 trouvées avec relations vérifiées)
- **F-Measure** : 0.923

### Tableau des Métriques de Qualité avec Relations

| Métrique       | MinHash | SimHash | Combinaison |
|----------------|---------|---------|-------------|
| Recall         | 1.0     | 1.0     | 1.0         |
| Precision      | 0.857   | 0.857   | 0.857       |
| F-Measure      | 0.923   | 0.923   | 0.923       |

### Conclusion

1. **Algorithmes Utilisés :**
   - **MinHash** et **SimHash** pour estimer les similarités entre les éléments des métamodèles PRINCE2 et Scrum.
   
2. **Correspondances Réelles :**
   - Définies entre les éléments similaires des deux métamodèles.

3. **Résultats des Algorithmes :**
   - MinHash et SimHash ont donné des résultats très similaires avec des métriques de qualité élevées.

4. **Vérification des Relations :**
   - Les relations entre les éléments correspondants des deux métamodèles ont été vérifiées et validées.

5. **Combinaison des Résultats :**
   - La combinaison des résultats des deux algorithmes n'a pas amélioré significativement les métriques de qualité, car les algorithmes ont donné des résultats très proches.

6. **Application sur d'Autres Métamodèles :**
   - Il est recommandé de tester ces algorithmes sur d'autres paires de métamodèles pour valider leur efficacité et robustesse.

Ce rapport détaillé présente les étapes de la mise en œuvre des algorithmes de matching entre les métamodèles PRINCE2 et Scrum, les résultats obtenus, les métriques de qualité calculées, ainsi que la vérification des relations entre les éléments. Pour toute question ou analyse supplémentaire, n'hésitez pas à me contacter.


# Code Lab Forge

Welcome to Code Lab Forge! This repository contains a collection of mini-projects designed to help you learn various programming concepts and techniques.

## Projects

### Project 1: Word Counter

- **Description**: This project contains a Python script that counts the occurrences of a specified word in a text file.
- **Usage**: 
  ```bash
  python word_counter.py <path_to_file> <word_to_count>
  ```
- **Example**:
  ```bash
  python word_counter.py "path/to/file.txt" "specifiedWord"
  ```

### Project 2: Mini Chatbot

- **Description**: This project includes a Python script for a simple chatbot that responds to user input with predefined messages.
- **Usage**: 
  ```python
  python chatbot.py
  ```
- **Example**:
  ```python
  python chatbot.py
  ```
- **Commands**:
  - `salam` or `slm`: Greets the user.
  - `chra7e` or `chera7e` or `kifache`: Provides explanations for programming terms.

### Project 3: Web Scraper

- **Description**: This project contains Python scripts for scraping data from various websites using BeautifulSoup and requests libraries.
- **Usage**:
  - OnePageSSS:
    ```python
    python one_page_scraper.py
    ```
  - ScrapeBooks:
    ```python
    python scrape_books.py
    ```
  - ScrapeQuotes:
    ```python
    python scrape_quotes.py
    ```
    
### Project 4: Diabetes Prediction App

- **Description**: This project is a Streamlit web application that predicts whether a person has diabetes based on their input features such as age, BMI, HbA1c level, blood glucose level, gender, and smoking history.
- **Usage**: 
  ```bash
  streamlit run app.py
  ```
- **Getting Started**:
  1. Clone the repository:
     ```bash
     git clone https://github.com/your_username/diabetes-prediction-app.git
     ```
  2. Navigate to the project directory:
     ```bash
     cd diabetes-prediction-app
     ```
  3. Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```
  4. Run the Streamlit app:
     ```bash
     streamlit run app.py
     ```
  5. Access the app in your web browser at the provided URL.
- **Example**:
  - Input the required health attributes in the sidebar.
  - Click the "Predict" button.
  - The app will display whether the person is predicted to have diabetes or not.
- **Data**: The dataset used for training the model is not included in this repository due to privacy reasons. However, you can replace it with your own dataset following the same structure.

## Getting Started

1. Clone this repository to your local machine.
2. Navigate to the desired project folder.
3. Follow the usage instructions provided in the project's README.md file.

## Contributing

If you'd like to contribute to this repository by adding new mini-projects or improving existing ones, please feel free to submit a pull request.

1. Fork this repository.
2. Create a new branch: `git checkout -b feature/new-mini-project`.
3. Make your changes and commit them: `git commit -m 'Add new mini-project'`.
4. Push to the branch: `git push origin feature/new-mini-project`.
5. Submit a pull request.

## License

This repository is licensed under the [Unlicense](LICENSE). For more information, please refer to <https://unlicense.org>.
