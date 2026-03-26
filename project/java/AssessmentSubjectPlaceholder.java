package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  Used when the assessment subjects will be determined as part of one or more other assessment activities.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AssessmentSubjectPlaceholder  {

  private String uuid;
  private String description;
  private List<AssessmentSubjectSource> sources;
  private String remarks;
  private List<Property> props;
  private List<Link> links;

}