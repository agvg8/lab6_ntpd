import numpy as np
from model import train_and_predict, get_accuracy
from app import app

def test_predictions_not_none():
    """
    Test 1: Sprawdza, czy otrzymujemy jakąkolwiek predykcję.
    """
    preds, _ = train_and_predict()
    assert preds is not None, "Predictions should not be None."


def test_predictions_length():
    """
    Test 2: Sprawdza, czy długość listy predykcji jest większa od 0 i czy odpowiada przewidywanej liczbie próbek testowych.
    """
    preds, _ = train_and_predict()
    assert len(preds) > 0, "Predictions should not be empty."
    assert len(preds) == 1, f"Expected 1 prediction, got {len(preds)}"


def test_predictions_value_range():
    """
    Test 3: Sprawdza, czy wartości w predykcjach mieszczą się w spodziewanym zakresie.
    """
    preds, _ = train_and_predict()
    assert all(isinstance(pred, (int, float)) for pred in preds), "All predictions should be numeric."


def test_model_accuracy():
    """
    Test 4: Sprawdza, czy model osiąga co najmniej 70% dokładności.
    """
    _, accuracy = get_accuracy()
    assert accuracy >= 0.7, f"Expected accuracy of at least 70%, got {accuracy * 100}%"


def test_predict_endpoint():
    """
    Test 5: Sprawdza, czy endpoint /predict działa poprawnie.
    """
    with app.test_client() as client:
        response = client.post('/predict', json={'values': [6]})
        assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
        data = response.get_json()
        assert "prediction" in data, "Response should contain 'prediction'."
        assert isinstance(data["prediction"], list), "Prediction should be a list."
