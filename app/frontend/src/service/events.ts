import { Timestamp } from "google-protobuf/google/protobuf/timestamp_pb";
import {
  CreateEventReq,
  OfflineEventInformation,
  OnlineEventInformation,
} from "proto/events_pb";
import client from "service/client";

interface EventInput {
  content: string;
  title: string;
  // To be figured out what the best type for these are with dayjs...
  startTime: Date;
  endTime: Date;
}

interface OnlineEventInput extends EventInput {
  isOnline: true;
  parentCommunityId: number;
  link: string;
}

interface OfflineEventInput extends EventInput {
  isOnline: false;
  address: string;
  lat: number;
  lng: number;
}

export type CreateEventInput = OnlineEventInput | OfflineEventInput;

export async function createEvent(input: CreateEventInput) {
  const req = new CreateEventReq();
  req.setTitle(input.title);
  req.setContent(input.content);
  req.setStartTime(Timestamp.fromDate(input.startTime));
  req.setEndTime(Timestamp.fromDate(input.endTime));
  // TODO: dayjs "magic" to figure out timezone string to send
  req.setTimezone("UTC");

  if (input.isOnline) {
    const onlineEventInfo = new OnlineEventInformation();
    onlineEventInfo.setLink(input.link);
    req.setParentCommunityId(input.parentCommunityId);
    req.setOnlineInformation(onlineEventInfo);
  } else {
    const offlineEventInfo = new OfflineEventInformation();
    offlineEventInfo.setAddress(input.address);
    offlineEventInfo.setLat(input.lat);
    offlineEventInfo.setLng(input.lng);
    req.setOfflineInformation(offlineEventInfo);
  }

  const res = await client.events.createEvent(req);
  return res.toObject();
}
