package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Represents a scheduled event or milestone, which may be associated with a series of assessment actions.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Task  {

  private String uuid;
  private String type;
  private String title;
  private String description;
  private EventTiming timing;
  private List<TaskDependency> dependencies;
  private List<AssociatedActivity> associated-activities;
  private List<Task> tasks;
  private List<AssessmentSubject> subjects;
  private String remarks;
  private List<ResponsibleRole> responsible-roles;
  private List<Property> props;
  private List<Link> links;

}