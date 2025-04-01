import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.ack_container import AckContainer  # noqa: E501
from openapi_server.models.ext_key_container import ExtKeyContainer  # noqa: E501
from openapi_server.models.message_data import MessageData  # noqa: E501
from openapi_server.models.version_container import VersionContainer  # noqa: E501
from openapi_server.models.void_container import VoidContainer  # noqa: E501
from openapi_server import util


def get_versions():  # noqa: E501
    """Get supported API versions

    Return list of supported ETSI GS QKD 020 API versions.  When an SAE makes a request to a KME, it should use the most recent version of the API that the KME and SAE support.  The SAE can use this end-point to determine which API versions the KME supports.  # noqa: E501


    :rtype: Union[VersionContainer, Tuple[VersionContainer, int], Tuple[VersionContainer, int, Dict[str, str]]
    """
    return 'do some magic!'


def post_ext_keys(body):  # noqa: E501
    """Transfer keys to external KMS

    Pass an extended key request container comprising key material and associated data to another KME, for the key(s) to be delivered (by relay where necessary) to the target SAE(s) specified. The extended key request container contains keys matching those to be delivered to the initiator SAE.  This method is &#39;non-blocking&#39;. Upon a valid request, the KME will respond with an HTTP code 202 (&#39;Accepted&#39;), then it will issue a separate call (or multiple calls) to the specified &#x60;ack_callback_url&#x60; endpoint once the keys are actually delivered (or fail to be delivered).  A Code 400 error will be returned if the container format is invalid or includes initiator/target SAE IDs for which a valid route is not known to the KME.  # noqa: E501

    :param ext_key_container: Extended key request container.
    :type ext_key_container: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    ext_key_container = body
    if connexion.request.is_json:
        ext_key_container = ExtKeyContainer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_ext_keys_ack(body):  # noqa: E501
    """Acknowledge completion of a previous ext_key request

    Pass one or more key acknowledgement container comprising key IDs associated with a previous call to the ext_keys method by an external KMS. The status of all keys in the container is indicated by the status field.  The &#x60;ack_status&#x60; field may be &#x60;relayed&#x60; &#x60;voided&#x60; &#x60;failed&#x60; or &#x60;key not present&#x60;.  - &#x60;relayed&#x60; indicates the KME has successfully relayed the specified keys to the requested target (where the initiator_sae_id and target_sae_id are specified in the acknowledgement container). If the initiator requested multiple targets, the acknowledgements for each target are separate acknowledgement containers (since the status for each target may be different).  - &#x60;voided&#x60; indicates the KME has successfully voided the specified keys so they will not be delivered to applications.  - &#x60;failed&#x60; indicates that the requested operation on the specified keys could not be completed. For example, an ext_keys request may not complete if there is insufficient key material for relaying. Also, a void request will fail if the specified keys have already been delivered to a requesting SAE.  - &#x60;key not present&#x60; indicates that the specified keys could not be found by the KME.  In addition to the &#x60;status&#x60; field, additional information (e.g. explaining a failure) can be included in the optional &#x60;message&#x60; field.  It is possible that a single ext_keys request included multiple keys, where some are successfully delivered and other fail. This can be indicated by a KME sending multiple acknowledgement requests, with the container payload used to specify the status of different arrays of keys. A single container should be used for each target SAE ID.  Extension fields may also be optionally included (which could be, e.g. metadata for each key to indicate its routing information from the remote KMS). If such extensions are included, the extensions should be handled accordingly (e.g. to keep the provided metadata with each key so it can be relayed to the initiator SAE).  A Code 200 Success will returned by a KME receiving a valid acknowledgement, otherwise an Error Code will be returned including details of the error.  # noqa: E501

    :param ack_container: Acknowledgements containers
    :type ack_container: list | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    ack_container = body
    if connexion.request.is_json:
        ack_container = [AckContainer.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def post_ext_keys_void(body, all_confirmation=None):  # noqa: E501
    """Signal keys as void to external KMS (i.e. discard keys)

    Pass an extended key request container comprising key IDs to another KME, for the key(s) to be marked as void (i.e. discarded and not delivered to SAEs). The Extended Key Container contains keys matching those already passed to the KME.  As for &#x60;ext_keys&#x60;, this method is &#39;non-blocking&#39;. Upon a valid request, a KME shall discard keys relating to the provided key IDs and post a call to the specified &#x60;ack_callback_url&#x60; describing the completed operation. Any subsequent &#39;get key with key ID&#39; requests made to the KME (using ETSI 014) for those keys will be rejected.  A Code 400 error will be returned if the container format is invalid or includes initiator/target SAE IDs for which a valid route is not known to the KME.  If this is called without supplying a &#x60;key_ids&#x60; array, then all keys shared between the provided SAEs will be voided (to prevent accidental key loss, to confirm this action an &#x60;all_confirmation&#x60; boolean field must also be passed as true, otherwise a Code 400 error is returned).  # noqa: E501

    :param void_container: Void request container
    :type void_container: dict | bytes
    :param all_confirmation: Confirmation flag used to confirm deletion of all keys when no key IDs are specified.
    :type all_confirmation: bool

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    void_container = body
    if connexion.request.is_json:
        void_container = VoidContainer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
