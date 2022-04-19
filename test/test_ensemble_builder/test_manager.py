from __future__ import annotations

from typing import Callable

from autosklearn.automl import AutoML
from autosklearn.ensemble_building import EnsembleBuilderManager

from pytest_cases import parametrize_with_cases
from unittest.mock import MagicMock, patch

import test.test_automl.cases as cases
from test.conftest import DEFAULT_SEED


@parametrize_with_cases("automl", cases=cases, has_tag="fitted")
def case_real_runs(
    automl: AutoML,
    make_ensemble_builder_manager: Callable[..., EnsembleBuilderManager],
) -> EnsembleBuilderManager:
    """Uses real runs from a fitted automl instance"""
    manager = make_ensemble_builder_manager(
        backend=automl._backend,
        metric=automl._metric,
        task=automl._task,
        dataset_name=automl._dataset_name,
        seed=automl._seed,
        logger_port=automl._logger_port,
        random_state=DEFAULT_SEED,
    )
    return manager


@parametrize_with_cases("manager", cases=case_real_runs)
def test_run_builds_valid_ensemble(manager: EnsembleBuilderManager) -> None:
    ...


@parametrize_with_cases("builder", cases=case_real_runs)
def test_main(builder: EnsembleBuilderManager) -> None:
    ...
