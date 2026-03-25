package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Identifies an individual task for which the containing object is a consequence of.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RelatedTask  {

  private String task-uuid;
  private List<AssessmentSubject> subjects;
  private IdentifiedSubject identified-subject;
  private String remarks;
  private List<ResponsibleParty> responsible-parties;
  private List<Property> props;
  private List<Link> links;

}