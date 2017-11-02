import case
import datetime


document = case.Document()

instrument = document.create_uco_object(
    'Tool',
    name='Super Forensic Tool 3000',
    version='3.4.5',
    toolType='Extraction',
    creator='Frank Grimes')

performer = document.create_uco_object('Identity')
performer.create_property_bundle(
    'SimpleName',
    givenName='John',
    familyName='Doe')

action = document.create_uco_object(
    'ForensicAction',
    startTime=datetime.datetime(2017, 7, 21, 13, 32),
    endTime=datetime.datetime(2017, 7, 21, 14, 12))
action.create_property_bundle(
    'ActionReferences',
    performer=performer,
    instrument=instrument,
    # object and result should be filled with
    # input and output uco objects for this Forensic action.
    object=None,
    result=[])

document.serialize(format='json-ld', destination='output.json')
