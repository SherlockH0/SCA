from typing import Any

from rest_framework import serializers

from missions.models import Mission, Target


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ["id", "name", "country", "notes", "complete"]

    def validate(self, attrs: dict[str, Any]) -> dict[str, Any]:
        if (
            "notes" in attrs
            and self.instance
            and (self.instance.complete or self.instance.mission.complete)
        ):
            raise serializers.ValidationError(
                {"notes": "Can't add notes to completed target"}
            )
        return super().validate(attrs)


class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "complete", "targets", "cat"]
        model = Mission

    def validate(self, attrs: dict[str, Any]) -> dict[str, Any]:
        validated_data = super().validate(attrs)
        cat = validated_data.get("cat") or self.instance.cat
        if (
            cat
            and cat.missions.filter(complete=False).exists()
            and validated_data.get("complete") is False
        ):
            raise serializers.ValidationError({"cat": "Cat is on a mission"})
        return validated_data


class FullMissionSerializer(MissionSerializer):
    targets = TargetSerializer(many=True)

    def validate_targets(self, targets):
        length = len(targets)
        if length == 0:
            raise serializers.ValidationError(
                {"targets:": "A mission must have at least one target"}
            )
        elif length > 3:
            raise serializers.ValidationError(
                {"targets:": "A mission can have at most 3 targets"}
            )
        return targets

    def create(self, validated_data: dict[str, Any]) -> Any:
        targes = validated_data.pop("targets")

        mission = super().create(validated_data)

        for target in targes:
            Target.objects.create(mission_id=mission.pk, **target)

        return mission
