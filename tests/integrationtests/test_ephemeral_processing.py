#!/usr/bin/env python
"""Copyright (c) 2018-2024 mundialis GmbH & Co. KG.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

First test
"""

__license__ = "GPLv3"
__author__ = "Anika Weinmann"
__copyright__ = "Copyright 2022 mundialis GmbH & Co. KG"
__maintainer__ = "mundialis GmbH & Co. KG"

from actinia_core.core.resource_data_container import ResourceDataContainer

from actinia_processing_lib.utils import try_import

BASE_URL_DATA = "https://apps.mundialis.de/actinia_test_datasets"
POLYGON_GML = f"{BASE_URL_DATA}/polygon.gml"
PROCESS_CHAIN_VECTOR_IMPORT_INFO = {
    "list": [
        {
            "id": "v_info",
            "inputs": [
                {
                    "import_descr": {
                        "source": POLYGON_GML,
                        "type": "vector",
                    },
                    "param": "map",
                    "value": "polygon",
                },
            ],
            "module": "v.info",
            "flags": "g",
        },
    ],
    "version": "1",
}


def test_ephemeral_processing() -> None:
    """Test basic processing."""
    # pylint: disable=invalid-name
    EphemeralProcessing = try_import(
        "actinia_processing_lib.ephemeral_processing",
        "EphemeralProcessing",
    )

    # 'grass_data_base', 'grass_user_data_base', 'grass_base_dir',
    # 'request_data', 'user_id', 'user_group', 'resource_id', 'iteration',
    # 'status_url', 'api_info', 'resource_url_base', 'orig_time',
    # 'orig_datetime', 'user_credentials', 'config', 'project_name',
    # 'mapset_name', and 'map_name'
    rdc = ResourceDataContainer(
        "/actinia_core/grassdb",
        "/actinia_core/userdata",
        "/usr/local/grass",
        PROCESS_CHAIN_VECTOR_IMPORT_INFO,
        "user",
        "user",
        "resource_id-1234",
        None,
        "http://localhost:8000/api/v1/status",
        {
            "endpoint": "asyncephemeralexportresource",
            "method": "POST",
            "path": "/api/v3/locations/nc_spm_08/processing_async_export",
            "request_url": "http://0.0.0.0:8088/api/v3/locations/nc_spm_08/"
            "processing_async_export",
        },
        "http://0.0.0.0:8088/api/v1/resource-id-1234/__None__",
        1749204596.1047864,
        "2025-06-06 10:09:56.104791",
        {
            "user_id": "user",
            "password_hash": "1234",
            "user_role": "user",
            "user_group": "user",
            "permissions": {
                "process_time_limit": 1800,
                "cell_limit": 1,
                "process_num_limit": 10,
                "accessible_modules": [
                    "v.info",
                ],
            },
        },
        {"LOG_LEVEL": 3, "AUTHENTICATION": False, "CHECK_CREDENTIALS": False},
        "nc_spm_08",
        None,
        None,
    )

    processing = EphemeralProcessing(rdc)
    processing.run()

    assert (
        processing.finish_message == "Processing successfully finished"
    ), "Expected 'Processing successfully finished', got "
    f"'{processing.finish_message}'"
    assert (
        processing.last_module == "v.info"
    ), f"Expected 'v.info', got '{processing.last_module}'"
    assert (
        processing.number_of_processes == 3
    ), f"Expected 3 processes, got {processing.number_of_processes}"
    assert processing.progress == {
        "step": 3,
        "num_of_steps": 3,
    }, "Expected progress to be {{'step': 3, 'num_of_steps': 3}}, got "
    f"{processing.progress}"
    assert (
        processing.progress_steps == 3
    ), f"Expected progress_steps to be 3, got {processing.progress_steps}"
    assert processing.run_state == {
        "success": None,
    }, "Expected run_state to be {{'success': None}}, got "
    f"{processing.run_state}"

    # (Pdb) dir(processing) # removed internal attributes
    # ['actinia_process_dict', 'actinia_process_list', 'api_info',
    # 'cell_limit', 'config', 'data', 'finish_message', 'ginit',
    # 'ginit_tmpfiles', 'global_project_path', 'grass_base_dir',
    # 'grass_data_base', 'grass_temp_database', 'grass_user_data_base',
    # 'has_fluent', 'interim_result', 'is_global_database', 'iteration',
    # 'last_module', 'lock_interface', 'map_name', 'mapset_name',
    # 'message_logger', 'module_output_dict', 'module_output_log',
    # 'module_results', 'number_of_processes', 'orig_datetime', 'orig_time',
    # 'output_parser_list', 'proc_chain_converter', 'process_chain_list',
    # 'process_count', 'process_dict', 'process_num_limit',
    # 'process_time_limit', 'progress', 'progress_steps', 'project_name',
    # 'rdc', 'request_data', 'required_mapsets', 'resource_export_list',
    # 'resource_id', 'resource_logger', 'resource_url_list',
    # 'response_model_class', 'run', 'run_state', 'setup_flag',
    # 'skip_region_check', 'status_url', 'temp_file_count', 'temp_file_path',
    # 'temp_grass_data_base', 'temp_grass_data_base_name', 'temp_mapset_name',
    # 'temp_mapset_path', 'temp_project_path', 'temporary_pc_files',
    # 'unique_id', 'user_credentials', 'user_group', 'user_id',
    # 'user_project_path', 'webhook_auth', 'webhook_finished',
    # 'webhook_update']
